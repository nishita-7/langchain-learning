from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Temperature is a creativity parameter - Controls the randomness of a LM's output
# max_completion_tokens - Number of words in the response - Helpful for limiting / controlling the token usage 
model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=10)

result = model.invoke("What is the capital of India")
print(result) # Prints other fields as well like tokens used, etc.
print(result.content) # Prints only the answer to the prompt