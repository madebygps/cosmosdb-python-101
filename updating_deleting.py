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

# read an individual item to replace

# book = container_client.read_item('b9f2e8d7-3c4a-4b1f-95e6-7a8d2f10c5e9','Fiction')
# print(f'tags before: {book['tags']}')
# book['tags'].append('bestseller')
# updated_book = container_client.replace_item(book['id'], book)
# print(f'updated tags: {updated_book['tags']}')

# delete an item
container_client.delete_item('c672e38a-bfe8-466b-b7f1-f9d9352872e5', 'Classic Literature')