
import os
from azure.identity import DefaultAzureCredential
from azure.cosmos import CosmosClient
from dotenv import load_dotenv

load_dotenv()
ENDPOINT = os.getenv('COSMOS_ENDPOINT')
DATABASE_NAME = os.getenv('DATABASE_NAME')
CONTAINER_NAME = os.getenv('CONTAINER_NAME')

credential = DefaultAzureCredential()

client = CosmosClient(ENDPOINT, credential)
db_client = client.get_database_client(DATABASE_NAME)
container_client = db_client.get_container_client(CONTAINER_NAME)

# basic filter by property

query = "SELECT * FROM c WHERE c.category = 'Fiction'"
items = list(container_client.query_items(query))
print(f'Found {len(items)} fiction books')

# parameterized query - prevents sql injections

query = "SELECT * FROM c WHERE c.rating >= @min_rating"
params = [{"name": "@min_rating", "value": 4.5}]
items = list(container_client.query_items(query, params, enable_cross_partition_query=True))
print(f'Found {len(items)} books with high rating')

# Projection - select specific fields only

query = "SELECT c.id, c.title FROM c WHERE c.pageCount > @page_count"
params = [{"name": "@page_count", "value": 500}]
items = list(container_client.query_items(query, params, enable_cross_partition_query=True))
for item in items:
    print(f'{item}')
    
# Projection - select specific fields only

query = "SELECT * FROM c WHERE ARRAY_CONTAINS(c.tags, LOWER(@tag), true)"
params = [{"name": "@tag", "value": 'BESTSELLER'}]
items = list(container_client.query_items(query, params, enable_cross_partition_query=True))
print(f'Found {len(items)} with bestseller tag')


