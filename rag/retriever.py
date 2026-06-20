import pickle

import faiss
from sentence_transformers import SentenceTransformer

INDEX_PATH = "earth_intelligence.index"
CHUNKS_PATH = "chunks.pkl"

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

index = faiss.read_index(
    INDEX_PATH
)

with open(CHUNKS_PATH, "rb") as f:

    chunks = pickle.load(f)

def retrieve(
    query: str,
    k: int = 5
):

    query_embedding = model.encode(
        [query]
    )

    distances, indices = index.search(
        query_embedding,
        k
    )

    results = []

    for idx in indices[0]:

        results.append(
            chunks[idx]
        )

    return results