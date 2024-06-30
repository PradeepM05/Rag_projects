from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from bs4 import BeautifulSoup
import requests

import os
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT']  = 'https://api.smith.langchain.com'
os.environ['LANGCHAIN_API_KEY']='lsv2_pt_xxxxxxxx'
os.environ['OPEN_API_KEY']='sk-xxxxxxxxxxxx'

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


url = 'https://blog.langchain.dev/announcing-langsmith/'

#added in runnable pass through
#page_content = scrape_text(url)[:10000]

chain = RunnablePassthrough.assign(
    text = lambda x: scrape_text(x["url"])[:10000]
) | SUMMARY_PROMPT | ChatOpenAI(model='gpt-3.5-turbo-0125', temperature=0, openai_api_key = os.environ['OPEN_API_KEY'] ) | StrOutputParser()


# Define the input data
input_data = {
    "question": "What is langsmith?",
    "url": url
}

# Pass the required input argument
chain.invoke(input_data)

