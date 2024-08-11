![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-green.svg)
![License](https://img.shields.io/badge/license-CC%20BY%204.0-green.svg)

This repository contains a collection of Python scripts demonstrating how to use open-source embeddings with various vector databases. These cookbooks provide practical examples for data ingestion and similarity search using popular vector databases.

Vector databases are specialized database systems designed to store and query high-dimensional vectors efficiently. They are crucial for machine learning applications, particularly in natural language processing and computer vision.

## Table of Contents

1.[About Vector Database Cloud](#about-vector-database-cloud)
2. [Introduction](#introduction)
3. [Supported Vector Databases](#supported-vector-databases)
4. [Prerequisites](#prerequisites)
5. [Installation](#installation)
6. [Dependencies](#dependencies)
7. [Usage](#usage)
8. [Cookbooks](#cookbooks)
9. [Customization](#customization)
10. [Best Practices](#best-practices)
11. [Troubleshooting](#troubleshooting)
12 [Contributing](#contributing)
13. [Related Resources](#related-resources)
14. [License](#license)
15. [Disclaimer](#disclaimer)


## About Vector Database Cloud

[Vector Database Cloud](https://vectordbcloud.com) is a platform that provides one-click deployment of popular vector databases including Qdrant, Milvus, ChromaDB, and Pgvector on cloud. Our platform ensures a secure API, a comprehensive customer dashboard, efficient vector search, and real-time monitoring.

## Introduction

Vector Database Cloud is designed to seamlessly integrate with your existing data workflows. Whether you're working with structured data, unstructured data, or high-dimensional vectors, you can leverage popular ETL (Extract, Transform, Load) tools to streamline the process of moving data into and out of Vector Database Cloud.

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


## License

This work is licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0).

Copyright (c) 2024 Vector Database Cloud

You are free to:
- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material for any purpose, even commercially

Under the following terms:
- Attribution — You must give appropriate credit to Vector Database Cloud, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests Vector Database Cloud endorses you or your use.

Additionally, we require that any use of this guide includes visible attribution to Vector Database Cloud. This attribution should be in the form of "Open Source Embedding curated by Vector Database Cloud" or "Based on Vector Database Cloud Open Source Embedding", along with a link to https://vectordbcloud.com, in any public-facing applications, documentation, or redistributions of this guide.

No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

For the full license text, visit: https://creativecommons.org/licenses/by/4.0/legalcode


## Disclaimer

The information and resources provided in this community repository are for general informational purposes only. While we strive to keep the information up-to-date and correct, we make no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability or availability with respect to the information, products, services, or related graphics contained in this repository for any purpose. Any reliance you place on such information is therefore strictly at your own risk.

Vector Database Cloud configurations may vary, and it's essential to consult the official documentation before implementing any solutions or suggestions found in this community repository. Always follow best practices for security and performance when working with databases and cloud services.

The content in this repository may change without notice. Users are responsible for ensuring they are using the most current version of any information or code provided.

This disclaimer applies to Vector Database Cloud, its contributors, and any third parties involved in creating, producing, or delivering the content in this repository.

The use of any information or code in this repository may carry inherent risks, including but not limited to data loss, system failures, or security vulnerabilities. Users should thoroughly test and validate any implementations in a safe environment before deploying to production systems.

For complex implementations or critical systems, we strongly recommend seeking advice from qualified professionals or consulting services.

By using this repository, you acknowledge and agree to this disclaimer. If you do not agree with any part of this disclaimer, please do not use the information or resources provided in this repository.
