import os
import sys
from qdrant_client import QdrantClient
from qdrant_client.http import models
from sentence_transformers import SentenceTransformer

def main():
    # Get API URL and key from environment variables
    API_URL = os.getenv('VECTORDBCLOUD_QDRANT_API_URL')
    API_KEY = os.getenv('VECTORDBCLOUD_QDRANT_API_KEY')

    if not API_URL or not API_KEY:
        print("Error: API URL or API Key not set in environment variables.")
        sys.exit(1)

    try:
        # Initialize Qdrant client
        client = QdrantClient(url=API_URL, api_key=API_KEY)

        # Initialize the sentence transformer model (open-source embeddings)
        model = SentenceTransformer('all-MiniLM-L6-v2')
        vector_size = model.get_sentence_embedding_dimension()

        # Define collection name
        collection_name = "document_collection"

        # Create a new collection (or recreate if it already exists)
        client.recreate_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
        )

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

        # Prepare points for insertion
        points = [
            models.PointStruct(
                id=i,
                vector=embedding.tolist(),
                payload={"text": text}
            )
            for i, (text, embedding) in enumerate(zip(documents, embeddings))
        ]

        # Insert points
        client.upsert(
            collection_name=collection_name,
            points=points
        )

        print(f"Inserted {len(documents)} documents into Qdrant collection '{collection_name}'")

        # Perform a similarity search
        query = "What is the meaning of life?"
        query_embedding = model.encode([query])[0].tolist()

        search_result = client.search(
            collection_name=collection_name,
            query_vector=query_embedding,
            limit=3
        )

        print("\nTop 3 similar documents:")
        for i, point in enumerate(search_result):
            print(f"{i+1}. Text: {point.payload['text']}")
            print(f"   Score: {point.score}\n")

        print("Qdrant cookbook example completed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
