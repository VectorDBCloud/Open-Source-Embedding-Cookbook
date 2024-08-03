![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

This repository contains a collection of Python scripts demonstrating how to use open-source embeddings with various vector databases. These cookbooks provide practical examples for data ingestion and similarity search using popular vector databases.

Vector databases are specialized database systems designed to store and query high-dimensional vectors efficiently. They are crucial for machine learning applications, particularly in natural language processing and computer vision.

## Table of Contents

- [Supported Vector Databases](#supported-vector-databases)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Cookbooks](#cookbooks)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

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

Before running any script, set the appropriate environment variables:

```
export VECTORDBCLOUD_<DATABASE>_API_URL="https://your-vector-db-cloud-url.com"
export VECTORDBCLOUD_<DATABASE>_API_KEY="your-api-key"
```

Replace `<DATABASE>` with the specific database name (e.g., PGVECTOR, MILVUS, CHROMADB, QDRANT).

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


## Contribution and Feedback

We encourage contributions to enhance these cookbook examples. For contributing new scripts or suggesting improvements, please refer to our [Contribution Guidelines](CONTRIBUTING.md). If you encounter issues or have suggestions, please use the issue tracker.


## Disclaimer

These scripts are provided as examples and may need to be adapted to your specific use case and production environment. They are not guaranteed to work in all scenarios and should be thoroughly tested before use in any critical or production systems. Always follow best practices for security and performance when working with databases and APIs. The authors and contributors of this repository are not responsible for any damages or losses that may result from the use of these scripts.

Vector Database Cloud configurations may vary, and it's essential to consult the official documentation and your system administrators before running these scripts in your environment. Ensure you have the necessary permissions and understand the potential impact of each operation on your data and system resources.
