from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

# You send additional information about the format in the prompt 
# This information is provided by the Output Parser 
# It is called partial variables since it doesnt get filled at runtime, it gets filled before it 
template = PromptTemplate(
    template="Give me the name, age and city of a fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# prompt = template.format()
# print(prompt)

# result = model.invoke(prompt)
# print(result)

# final_result = parser.parse(result.content)

chain = template | model | parser
result = chain.invoke({}) # No input variables -> Pass an empty dictionary

print(result)

# Cannot enforce any schema 