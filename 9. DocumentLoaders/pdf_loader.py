# PyPDFLoader 
# Used to load cotnent from PDF files and convert each page into a Document object 
# {
#    Document(page_content='Text from page 1', metadata={'source': 'file.pdf', 'page': 1}),
#    Document(page_content='Text from page 2', metadata={'source': 'file.pdf', 'page': 2})
# }
# Limitations: Uses the PyPDF library under the hood - not great with scanned PDFs or complex layouts

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

print(docs)
print(len(docs))

print(docs[0].page_content) # Output: Text content of the first page of the PDF
print(docs[1].metadata) # Output: {'source': 'dl-curriculum.pdf', 'page': 2} - Metadata indicating the source file and page number for the second page of the PDF
