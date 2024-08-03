import os
import sys
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

def main():
    # Get API URL and key from environment variables
    API_URL = os.getenv('VECTORDBCLOUD_CHROMADB_API_URL')
    API_KEY = os.getenv('VECTORDBCLOUD_CHROMADB_API_KEY')

    if not API_URL or not API_KEY:
        print("Error: API URL or API Key not set in environment variables.")
        sys.exit(1)

    try:
        # Initialize ChromaDB client
        client = chromadb.Client(Settings(
            chroma_api_impl="rest",
            chroma_server_host=API_URL,
            chroma_server_http_port="443",
            chroma_server_ssl_enabled=True,
            chroma_server_headers={"X-Api-Key": API_KEY}
        ))

        # Initialize the sentence transformer model (open-source embeddings)
        model = SentenceTransformer('all-MiniLM-L6-v2')

        # Create or get a collection
        collection_name = "document_collection"
        collection = client.get_or_create_collection(name=collection_name)

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

        # Prepare metadata (optional)
        metadatas = [{"source": "proverb"} for _ in documents]

        # Add data to the collection
        collection.add(
            documents=documents,
            embeddings=embeddings.tolist(),
            metadatas=metadatas,
            ids=[f"doc{i}" for i in range(len(documents))]
        )

        print(f"Inserted {len(documents)} documents into ChromaDB collection '{collection_name}'")

        # Perform a similarity search
        query = "What is the meaning of life?"
        query_embedding = model.encode([query])[0].tolist()

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=3
        )

        print("\nTop 3 similar documents:")
        for i, (doc, metadata, distance) in enumerate(zip(results['documents'][0], results['metadatas'][0], results['distances'][0])):
            print(f"{i+1}. Document: {doc}")
            print(f"   Metadata: {metadata}")
            print(f"   Distance: {distance}\n")

        print("ChromaDB cookbook example completed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
