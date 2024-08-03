import os
from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility
from sentence_transformers import SentenceTransformer

# Get API URL and key from environment variables
API_URL = os.getenv('VECTORDBCLOUD_MILVUS_API_URL')
API_KEY = os.getenv('VECTORDBCLOUD_MILVUS_API_KEY')

# Connect to Milvus
connections.connect("default", uri=API_URL, token=API_KEY)

# Initialize the sentence transformer model (open-source embeddings)
model = SentenceTransformer('all-MiniLM-L6-v2')
dim = model.get_sentence_embedding_dimension()

# Define collection name
collection_name = "document_collection"

# Define the collection schema
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="content", dtype=DataType.VARCHAR, max_length=500),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=dim)
]
schema = CollectionSchema(fields, "Documents with embeddings")

# Create the collection
collection = Collection(collection_name, schema)

# Create an IVF_FLAT index for the embedding field
index_params = {
    "metric_type": "L2",
    "index_type": "IVF_FLAT",
    "params": {"nlist": 128}
}
collection.create_index("embedding", index_params)

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

# Insert the data
entities = [
    documents,  # content
    embeddings.tolist()  # embedding
]

collection.insert(entities)

# Flush the collection to ensure data is written
collection.flush()

print(f"Inserted {len(documents)} documents into Milvus collection '{collection_name}'")

# Perform a similarity search
query = "What is the meaning of life?"
query_embedding = model.encode([query])[0].tolist()

search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
results = collection.search(
    data=[query_embedding],  # query vector
    anns_field="embedding",
    param=search_params,
    limit=3,
    expr=None,
    output_fields=["content"]
)

print("\nTop 3 similar documents:")
for i, hit in enumerate(results[0]):
    print(f"{i+1}. Content: {hit.entity.get('content')}")
    print(f"   Distance: {hit.distance}\n")

# Disconnect from Milvus
connections.disconnect("default")

print("Milvus cookbook example completed successfully.")
