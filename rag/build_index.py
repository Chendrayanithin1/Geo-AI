from pathlib import Path
import pickle

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

KB_DIR = Path("knowledge_base")
INDEX_PATH = "earth_intelligence.index"
CHUNKS_PATH = "chunks.pkl"

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

chunks = []

for md_file in KB_DIR.rglob("*.md"):

    with open(md_file, "r", encoding="utf-8") as f:

        text = f.read()

    paragraphs = [
        p.strip()
        for p in text.split("\n\n")
        if p.strip()
    ]

    for para in paragraphs:

        chunks.append(
            {
                "source": md_file.name,
                "text": para
            }
        )

texts = [x["text"] for x in chunks]

embeddings = model.encode(
    texts,
    convert_to_numpy=True
)

index = faiss.IndexFlatL2(
    embeddings.shape[1]
)

index.add(
    np.array(embeddings)
)

faiss.write_index(
    index,
    INDEX_PATH
)

with open(CHUNKS_PATH, "wb") as f:
    pickle.dump(chunks, f)

print(
    f"Indexed {len(chunks)} chunks"
)