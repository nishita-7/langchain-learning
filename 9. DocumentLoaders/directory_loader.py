# Directory Loader 
# Document loader that lets you load multiple documents from a directory (folder) of files.

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books', 
    glob='*.pdf', # Pattern to match files (e.g. '*.pdf' for PDF files, '*.txt' for text files, etc.)
    loader_cls=PyPDFLoader
)

# docs = loader.load()

# print(len(docs)) # Output: Number of documents loaded
# print(docs[0].page_content) # Output: First document loaded
# print(docs[0].metadata) # Output: Metadata of the first document (e.g. file name, page number, etc.)

# print(docs[766].page_content) # Output: Last document loaded
# print(docs[766].metadata) # Output: Metadata of the last document (e.g. file name, page number, etc.)

docs = loader.lazy_load() # Load documents lazily (i.e. load one document at a time when needed)

for document in docs:
    print(document.page_content) # The actual text content of each document
    print(document.metadata) # Metadata associated with each document (e.g. file name, page number, etc.)