# CosmosDB Python 101

A beginner-friendly guide to using Azure Cosmos DB with Python, demonstrating basic CRUD operations and queries.

## Prerequisites

- Azure Cosmos DB account No SQL
  - Name your account what ever you'd like, mine is named `bookrecommender`
  - Create a database, name it whatever you'd like, mine is `BookRecommendationsDB`
  - Create a container named `books` and `/category` as the partition key
  - Insert the items from the [items folder](items/) into your container
- Azure CLI installed and logged in
- [Azure Identity with permissions to access the Cosmos DB account](https://learn.microsoft.com/azure/cosmos-db/nosql/security/how-to-grant-data-plane-role-based-access?tabs=built-in-definition%2Ccsharp&pivots=azure-interface-cli)
- Python 3.11 or higher
- Required Python packages:
  - azure-cosmos
  - azure-identity
  - python-dotenv

## Environment Setup

Update the `.env-sample` with your values and rename it to `.env`

## Scripts

### 1. setup.py

A basic script that demonstrates connecting to Cosmos DB and listing all databases and their containers using Azure Identity authentication.

```sh
python setup.py
```

### 2. creating_reading.py

A script that demonstrates basic reading and creation operations:

- Reading all items from a container
- Reading a single item by ID and partition key
- Creating a new item with a complex schema including nested objects and arrays

```sh
python creating_reading.py
```

### 3. updating_deleting.py

A script showing how to modify and remove data:

- Updating an existing item using replace operation
- Deleting items by ID and partition key

```sh
python updating_deleting.py
```

### 4. querying.py

A comprehensive script demonstrating various querying capabilities:

- Basic filtering using WHERE clause
- Parameterized queries for safe value injection
- Projections to select specific fields
- Array contains operations with case-insensitive search
- Cross-partition queries

```sh
python querying.py
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
