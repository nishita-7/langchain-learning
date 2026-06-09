from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

loader = PyPDFLoader("dl-curriculum.pdf")

docs = loader.load()

# Create a splitter object 
splitter = CharacterTextSplitter(
    chunk_size=100, # The maximum size of each chunk
    chunk_overlap=0, # The number of characters to overlap between chunks
    separator=' ' # The character to use as a separator when splitting the text
)

# result = splitter.split_text(text)
result = splitter.split_documents(docs)

print(result) # A list of Document objects, each containing a chunk of text
print(result[0]) # The first chunk as a Document object
print(result[0].page_content) # The content of the first chunk