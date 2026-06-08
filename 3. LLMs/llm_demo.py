from langchain_openai import OpenAI

# Helps to load the api key from the .env
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

# Invoke is a very important function - Helps to communicate with the model
result = llm.invoke("What is the capital of India") # Gives the prompt to the model & gets back the reply 

print(result)