import chromadb
from sentence_transformers import SentenceTransformer
import pandas as pd

model = SentenceTransformer("all-MiniLM-L6-v2")  # free, runs locally
client = chromadb.Client()

def index_dataframe(df: pd.DataFrame, collection_name="bi_data"):
    collection = client.get_or_create_collection(collection_name)
    texts = df.astype(str).apply(lambda row: " | ".join(row), axis=1).tolist()
    embeddings = model.encode(texts).tolist()
    ids = [str(i) for i in range(len(texts))]
    collection.add(documents=texts, embeddings=embeddings, ids=ids)
    return collection

def query_store(question: str, collection_name="bi_data", n=5):
    collection = client.get_collection(collection_name)
    embedding = model.encode([question]).tolist()
    results = collection.query(query_embeddings=embedding, n_results=n)
    return results["documents"][0]
