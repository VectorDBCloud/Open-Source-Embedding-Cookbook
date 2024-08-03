import os
import psycopg2
import numpy as np
from sentence_transformers import SentenceTransformer

# Get API URL and key from environment variables
API_URL = os.getenv('VECTORDBCLOUD_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_API_KEY')

# Initialize the sentence transformer model (open-source embeddings)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample data
documents = [
    "The quick brown fox jumps over the lazy dog",
    "A journey of a thousand miles begins with a single step",
    "To be or not to be, that is the question",
    "All that glitters is not gold",
    "Where there's a will, there's a way"
]

# Generate embeddings using the open-source model
embeddings = model.encode(documents)

# Connect to the database using the API URL and key
conn = psycopg2.connect(API_URL, password=API_KEY)
cur = conn.cursor()

# Create table (if not exists)
cur.execute("""
CREATE TABLE IF NOT EXISTS documents (
    id SERIAL PRIMARY KEY,
    content TEXT,
    embedding vector(384)
)
""")

# Insert data
for doc, emb in zip(documents, embeddings):
    cur.execute(
        "INSERT INTO documents (content, embedding) VALUES (%s, %s)",
        (doc, emb.tolist())
    )

conn.commit()

print(f"Inserted {len(documents)} documents into pgvector.")

# Perform a similarity search
query = "What is the meaning of life?"
query_embedding = model.encode([query])[0]

cur.execute("""
SELECT content, 1 - (embedding <=> %s) AS similarity
FROM documents
ORDER BY similarity DESC
LIMIT 3
""", (query_embedding.tolist(),))

results = cur.fetchall()

print("\nTop 3 similar documents:")
for content, similarity in results:
    print(f"Similarity: {similarity:.4f}, Content: {content}")

# Close the connection
cur.close()
conn.close()

print("\npgvector cookbook example completed successfully.")
