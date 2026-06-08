from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "The cat sat on the mat",
    "Dogs are loyal animals",
    "Python is a popular programming language",
    "Machine learning is a subset of artificial intelligence",
    "The sun rises in the east",
    "Neural networks are inspired by the human brain",
]

query = "What is python?"

# Embed documents and query
doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

# Calculate similarity
similarities = cosine_similarity([query_embedding], doc_embeddings)[0]
# print(cosine_similarity([query_embedding], doc_embeddings))

# Print results sorted by similarity
# print(list(enumerate(scores)))
print(f"Query: {query}\n")
for doc, score in sorted(zip(documents, similarities), key=lambda x: x[1], reverse=True):
    print(f"Score: {score:.4f} | {doc}")