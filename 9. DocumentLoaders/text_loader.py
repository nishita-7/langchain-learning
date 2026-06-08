# TEXTLOADER
# Simple & commonly used 
# Reads plain text (.txt) files and converts them into Langchain Document objects.
# Use Case: Ideal for loading chat logs, scraped text, transcripts, code snippets or any plain text data into a LangChain pipeline
# Limitation: Works only with text data 

from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

print(docs) # Output: [Document(page_content='...', metadata={...})]
print(type(docs)) # Output: <class 'list'>
print(docs[0])
print(type(docs[0])) # Output: <class 'langchain_core.document.Document'>
print(docs[0].page_content) # Output: The actual text content of the document
print(docs[0].metadata) # Output: Metadata associated with the document (e.g

chain = prompt | model | parser 
print(chain.invoke({'poem': docs[0].page_content})) # Output: Summary of the poem