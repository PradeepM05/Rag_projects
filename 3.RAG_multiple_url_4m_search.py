#pip install langchain langchain_community openai duckduckgo-search beautifulsoup4 langchain_openai 
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from bs4 import BeautifulSoup
import requests
from langchain.utilities import DuckDuckGoSearchAPIWrapper

import os
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT']  = 'https://api.smith.langchain.com'
os.environ['LANGCHAIN_API_KEY']='lsv2_pt_xxxxxxxx'
os.environ['OPEN_API_KEY']='sk-xxxxxxxxxxxx'

#Number of urls to consider from duckduckgo search results
RESULTS_PER_QUESTION=3

#Function to retrieve top n results from duckduckgo search
def web_search(query: str, num_results: int=RESULTS_PER_QUESTION):
    ddg_search = DuckDuckGoSearchAPIWrapper()
    results = ddg_search.results(query, num_results)
    return [r["link"] for r in results]


summary_template = """ {text}
using the above text, answer the following question:
Question: {question}
if the question cannot be answered using the text, imply summarize the text. include all factual information, numbers, stats etc.
"""

SUMMARY_PROMPT = ChatPromptTemplate.from_template(summary_template)


def scrape_text(url: str):
  #send a GET request to webpage

  try:
    response = requests.get(url)

    #Check if request was successful
    if response.status_code == 200:
      #parse the HTML content with BeatifulSoup
      soup = BeautifulSoup(response.text, 'html.parser')

      #Extract all the text from the webpage
      page_text = soup.get_text(separator=" ", strip=True)

      return page_text
    else:
      return f"Failed to retrieve web page: Status code {response.status_code}"

  except Exception as e:
    print(e)
    return None


#url = 'https://blog.langchain.dev/announcing-langsmith/'    
#added in runnable pass through
#page_content = scrape_text(url)[:10000]

#Actual chain that takes one question and URL
scrape_and_summarize_chain = RunnablePassthrough.assign(
    text = lambda x: scrape_text(x["url"])[:10000]
) | SUMMARY_PROMPT | ChatOpenAI(model='gpt-3.5-turbo-0125', temperature=0, openai_api_key = os.environ['OPEN_API_KEY'] ) | StrOutputParser()


#Runnable chain that takes one question and extracts urls from websearch
chain = RunnablePassthrough.assign(
    urls = lambda x : web_search(x["question"])
) | (lambda x: [{"question":x["question"], "url":u}  for u in x["urls"]]) | scrape_and_summarize_chain.map()


# Define the input data
input_data = {
    "question": "What is langsmith?"
}

# Pass the required input argument
chain.invoke(input_data)

#Gets output from three sites
