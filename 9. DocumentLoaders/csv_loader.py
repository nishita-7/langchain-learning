# CSVLoader
# Used to load CSV files into Langchain Document objects - one per row, by default

from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='Social_Network_Ads.csv')

docs = loader.load()

print(len(docs)) # Output: Number of documents loaded (one per row in the CSV)
print(docs[1]) # Output: First document (first row of the CSV as a Document object)
print(docs) # Output: List of Document objects, each representing a row in the CSV with page_content as the row data and metadata containing column names and values