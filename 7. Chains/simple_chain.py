from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

prompt = PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

# Pipe operator: | -> LangChain Expression Language LCEL
chain = prompt | model | parser
result = chain.invoke({'topic':'ice hockey'})
print(result)

# Visualize the chain
chain.get_graph().print_ascii()