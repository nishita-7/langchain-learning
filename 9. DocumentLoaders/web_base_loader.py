# WebBaseLoader
# Used to load & extract text content from web pages (URLs)..
# Uses beautifulsoup4 under the hood to parse HTML content and extract valid text.
# Use Case: For blogs, news articles or public websites where the content is primarilt text-based & static.
# Limitations:
# 1. Doesn't handle JavaScript heavy pages well (use Selenium URL Loader for that).
# 2. Loads only static content (what's in the HTML, not what loads after the page renders).

from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://python.langchain.com/docs/introduction/'
loader = WebBaseLoader(url)

docs = loader.load()

# print(len(docs))
# print(docs[0].page_content)
# print(docs[0].page_content[:500]) # Print the first 500 characters of the extracted text content

chain = prompt | model | parser

print(chain.invoke({'question':'What is LangChain and what is it used for?', 'text':docs[0].page_content}))