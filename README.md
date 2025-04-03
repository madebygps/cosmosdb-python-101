# CosmosDB Python 101

A beginner-friendly guide to using Azure Cosmos DB with Python, demonstrating basic CRUD operations and queries.

## Prerequisites

- Azure Cosmos DB account 
- Azure CLI installed and logged in
- Azure Identity with permissions to access the Cosmos DB account
- Python 3.12 or higher
- Required Python packages (installed via `pyproject.toml`):
  - azure-cosmos
  - azure-identity
  - python-dotenv

## Environment Setup

Create a `.env` file with your Cosmos DB configuration:

```sh
COSMOS_ENDPOINT=<your-cosmos-endpoint>
DATABASE_NAME=<your-database-name>
BOOKS_CONTAINER=books
USER_PREFERENCES_CONTAINER=userPreferences
RECOMMENDATIONS_CONTAINER=recommendations
```

## Scripts

### 1. setup.py

A basic script that demonstrates connecting to Cosmos DB and listing all databases and their containers using Azure Identity authentication.

```sh
python setup.py
```

### 2. query.py

A more complex script showcasing common Cosmos DB operations:
- Reading all items from a container
- Reading a single item by ID
- Inserting new items
- Querying with SQL-like syntax
- Updating items
- Deleting items

```sh
python query.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.