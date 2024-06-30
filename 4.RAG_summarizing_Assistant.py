#pip install langchain langchain_community openai duckduckgo-search beautifulsoup4 langchain_openai  FastAPI sse_starlette uvicorn

from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from bs4 import BeautifulSoup
import requests
from langchain.utilities import DuckDuckGoSearchAPIWrapper
import json

import os
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT']  = 'https://api.smith.langchain.com'
os.environ['LANGCHAIN_API_KEY']='lsv2_pt_xxxxxxxx'
os.environ['OPEN_API_KEY']='sk-xxxxxxxxxxxx'

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

#Function to GET data from Web pages
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

#chain that takes one question and one url to generate text, added RunnablePassThrough second time to include references at the end
#scrape_and_summarize_chain = RunnablePassthrough.assign(
#    text = lambda x: scrape_text(x["url"])[:10000]
#) | SUMMARY_PROMPT | ChatOpenAI(model='gpt-3.5-turbo-0125', temperature=0, openai_api_key = os.environ['OPEN_API_KEY'] ) | StrOutputParser()

scrape_and_summarize_chain = RunnablePassthrough.assign(
    summary = RunnablePassthrough.assign(
        text = lambda x: scrape_text(x["url"])[:10000]
    ) | SUMMARY_PROMPT | ChatOpenAI(model='gpt-3.5-turbo-0125', temperature=0, openai_api_key = os.environ['OPEN_API_KEY'] ) | StrOutputParser()
) | (lambda x: f"URL: {x['url']}\n\nSummary: {x['summary']}")


#chain that takes one question and parsing multiple urls
web_search_chain = RunnablePassthrough.assign(
    urls = lambda x : web_search(x["question"])
) | (lambda x: [{"question":x["question"], "url":u}  for u in x["urls"]]) | scrape_and_summarize_chain.map()


SEARCH_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "user",
            "write 3 google search queries to search online that form an"
            "objective opinion from the following: {question}\n"
            "You must respond with a list of strings in the following format: "
            '["query 1", "query 2", "query 3"].',
        ),
    ]
)

#Chain that pulls three relavent question to given question
search_question_chain = SEARCH_PROMPT | ChatOpenAI(model='gpt-3.5-turbo-0125', openai_api_key = os.environ['OPEN_API_KEY'] ) | StrOutputParser() | json.loads
full_research_chain = search_question_chain | (lambda x : [{"question":q} for q in x]) | web_search_chain.map()

#Creating prompt to summarize all the oupts and generate a Thesis 
WRITER_SYSTEM_PROMPT = "You are an AI critical thinker research assistant. Your sole purpose is to write well written, critically acclaimed, objective and structured reports on given text."  # noqa: E501

# Report prompts from https://github.com/assafelovic/gpt-researcher/blob/master/gpt_researcher/master/prompts.py
RESEARCH_REPORT_TEMPLATE = """Information:
--------
{research_summary}
--------
Using the above information, answer the following question or topic: "{question}" in a detailed report -- \
The report should focus on the answer to the question, should be well structured, informative, \
in depth, with facts and numbers if available and a minimum of 1,200 words.
You should strive to write the report as long as you can using all relevant and necessary information provided.
You must write the report with markdown syntax.
You MUST determine your own concrete and valid opinion based on the given information. Do NOT deter to general and meaningless conclusions.
Write all used source urls at the end of the report, and make sure to not add duplicated sources, but only one reference for each.
You must write the report in apa format.
Please do your best, this is very important to my career."""  # noqa: E501


prompt = ChatPromptTemplate.from_messages(
    [
    ("system", WRITER_SYSTEM_PROMPT),
    ("user", REASEARCH_REPORT_TEMPLATE),
    ]
)

#Function to join the outputs which are within list of lists
def collapse_list_of_list(listoflists):
  content = []
  for l in listoflists:
    content.append("\n\n".join(l))
  return "\n\n".join(content)

#Final Chain to summarize the web search results and combine and generate a report as per research template
chain = RunnablePassthrough.assign(
    research_summary = full_research_chain | collapse_list_of_list 
) | prompt | ChatOpenAI(model='gpt-3.5-turbo-0125', temperature=0, openai_api_key = os.environ['OPEN_API_KEY'] ) | StrOutputParser()  



# Define the input data
input_data = {
    "question": "What is the difference between langsmith and langchain?"
}

# Pass the required input argument
chain.invoke(input_data)



#!/usr/bin/env python
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

add_routes(
    app,
    chain,
    path="/research-assistant",
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
