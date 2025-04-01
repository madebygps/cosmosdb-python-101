import os 
from azure.identity import DefaultAzureCredential
from azure.cosmos import CosmosClient
from dotenv import load_dotenv

load_dotenv()
ENDPOINT = os.getenv('COSMOS_ENDPOINT')

credential = DefaultAzureCredential()

try:
    client = CosmosClient(ENDPOINT, credential)
    for db in client.list_databases():
        print(f'Database name: {db['id']}')
except Exception as e:
    print(f'There was an error: {e}')