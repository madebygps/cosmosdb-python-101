import os

from azure.identity import DefaultAzureCredential
from azure.cosmos import CosmosClient
from dotenv import load_dotenv

load_dotenv()
ENDPOINT = os.getenv('COSMOS_ENDPOINT')
DATABASE_NAME = os.getenv('DATABASE_NAME')

credential = DefaultAzureCredential()

client = CosmosClient(ENDPOINT, credential)
db_client = client.get_database_client(DATABASE_NAME)

for container in db_client.list_containers():
    print(f'Container: {container['id']}')