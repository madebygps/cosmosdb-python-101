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
        db_client = client.get_database_client(db)
        for container in db_client.list_containers():
            print(f' - Container: {container['id']}')
except Exception as e:
    print(f'There was an error: {e}')