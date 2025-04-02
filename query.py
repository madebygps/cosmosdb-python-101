import os 
from azure.identity import DefaultAzureCredential
from azure.cosmos import CosmosClient
from dotenv import load_dotenv

load_dotenv()
ENDPOINT = os.getenv('COSMOS_ENDPOINT')
DATABASE_NAME = os.getenv('DATABASE_NAME')
CONTAINER_NAME = os.getenv('CONTAINER_NAME')
credential = DefaultAzureCredential()

try:
    client = CosmosClient(ENDPOINT, credential)
    db_client = client.get_database_client(DATABASE_NAME)
    container_client = db_client.get_container_client(CONTAINER_NAME)
    
    for item in container_client.read_all_items():
        print(item['id'])
    
except Exception as e:
    print(f'There was an error: {e}')