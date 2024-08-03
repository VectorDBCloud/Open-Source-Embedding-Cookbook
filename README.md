# Open-Source Embedding Cookbook

This repository contains a collection of Python scripts demonstrating how to use open-source embeddings with various vector databases. These cookbooks provide practical examples for data ingestion and similarity search using popular vector databases.

Vector databases are specialized database systems designed to store and query high-dimensional vectors efficiently. They are crucial for machine learning applications, particularly in natural language processing and computer vision.

## Supported Vector Databases

- [pgvector](https://github.com/pgvector/pgvector)
- [Milvus](https://milvus.io/)
- [ChromaDB](https://www.trychroma.com/)
- [Qdrant](https://qdrant.tech/)

## Prerequisites

- Python 3.7+
- Access to Vector Database Cloud (VectorDBCloud) with API URL and API key for each database

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/VectorDBCloud/Open-Source-Embedding-Cookbook.git
   cd Open-Source-Embedding-Cookbook
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Dependencies

The `requirements.txt` file includes the following main dependencies:
- sentence-transformers
- psycopg2-binary
- pymilvus
- chromadb
- qdrant-client

## Usage

Each cookbook is a standalone Python script demonstrating how to:
- Connect to the respective vector database
- Use open-source embeddings (Sentence Transformers with 'all-MiniLM-L6-v2' model)
- Insert sample data with embeddings
- Perform similarity searches

Before running any script, make sure to set the following environment variables:

[Environment variable setup instructions remain the same]

To run a cookbook:

```
python <cookbook_name>.py
```

For example:
```
python pgvector_cookbook.py
```

## Cookbooks

1. `pgvector_cookbook.py`: Demonstrates usage with pgvector
2. `milvus_cookbook.py`: Demonstrates usage with Milvus
3. `chromadb_cookbook.py`: Demonstrates usage with ChromaDB
4. `qdrant_cookbook.py`: Demonstrates usage with Qdrant

Each cookbook includes examples of:
- Connecting to the database
- Creating a collection/table
- Inserting sample data with embeddings
- Performing a similarity search

## Customization

To adapt these scripts for your own use case:
1. Replace the sample data with your own dataset.
2. Adjust the embedding model if needed (currently using 'all-MiniLM-L6-v2').
3. Modify the schema or collection structure to fit your data requirements.
4. Customize the similarity search query and parameters as per your needs.

## Troubleshooting

If you encounter issues:
1. Ensure all environment variables are correctly set.
2. Check your internet connection for API access.
3. Verify that you have the correct permissions for the Vector Database Cloud services.
4. Make sure all dependencies are correctly installed.

For specific error messages, please refer to the documentation of the respective vector database or create an issue in this repository.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

These scripts are provided as examples and may need to be adapted to your specific use case and production environment. Always follow best practices for security and performance when working with databases.
