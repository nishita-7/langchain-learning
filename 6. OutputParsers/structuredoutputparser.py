from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_classic.output_parsers.structured import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact_1', description="Fact 1 about the topic"),
    ResponseSchema(name='fact_2', description="Fact 2 about the topic"),
    ResponseSchema(name='fact_3', description="Fact 3 about the topic"),

]

parser = StructuredOutputParser.from_response_schemas(schema)

# You send additional information about the format in the prompt 
# This information is provided by the Output Parser 
# It is called partial variables since it doesnt get filled at runtime, it gets filled before it 
template = PromptTemplate(
    template="Give 3 facts about the {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# prompt = template.invoke({'topic': 'black hole'})

# result = model.invoke(prompt)
# final_result = parser.parse(result.content)
# print(final_result)

chain = template | model | parser
result = chain.invoke({'topic':'black hole'}) # No input variables -> Pass an empty dictionary
print(result)