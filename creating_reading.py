import os
import uuid
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

# read all items

for item in container_client.read_all_items():
    print(f'Title: {item['title']} ID: {item['id']} Category: {item['category']}')

# read an individual item

book = container_client.read_item('b9f2e8d7-3c4a-4b1f-95e6-7a8d2f10c5e9','Fiction')
print(book)

# create an item

new_book = {
    "id": str(uuid.uuid4()),
    "title": "Don Quixote",
    "author": "Miguel de Cervantes",
    "category": "Classic Literature",
    "publishedDate": "1605-01-16",
    "description": "The story follows the adventures of Alonso Quixano, a noble who loses his sanity after reading too many chivalric romances and decides to become a knight-errant under the name Don Quixote. Accompanied by his squire Sancho Panza, he sets out to revive chivalry and serve his nation.",
    "rating": 4.6,
    "tags": [
        "classic",
        "spanish literature",
        "satire",
        "adventure",
        "chivalry"
    ],
    "pageCount": 863,
    "isbn": "9780142437230",
    "imageUrl": "https://example.com/don-quixote-cover.jpg",
    "embeddings": {
        "contentVector": [
            0.345,
            -0.678,
            0.912,
            0.234,
            -0.567,
            0.890,
            -0.432,
            0.765
        ],
        "model": "text-embedding-ada-002",
        "version": "1.0"
    },
    "reviews": [
        {
            "userId": "c3d4e5f6-g7h8-i9j0-k1l2-m3n4o5p6q7r8",
            "rating": 5,
            "comment": "The first modern novel and still one of the greatest. A masterful blend of comedy, tragedy, and social commentary."
        }
    ]
}

container_client.create_item(new_book)

