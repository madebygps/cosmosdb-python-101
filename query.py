import os 
import uuid
from azure.identity import DefaultAzureCredential
from azure.cosmos import CosmosClient
from dotenv import load_dotenv

load_dotenv()
ENDPOINT = os.getenv('COSMOS_ENDPOINT')
DATABASE_NAME = os.getenv('DATABASE_NAME')
BOOKS_CONTAINER = os.getenv('BOOKS_CONTAINER')
USER_PREFERENCES_CONTAINER = os.getenv('USER_PREFERENCES_CONTAINER')
RECOMMENDATIONS_CONTAINER = os.getenv('RECOMMENDATIONS_CONTAINER')

credential = DefaultAzureCredential()

try:
    client = CosmosClient(ENDPOINT, credential)
    db_client = client.get_database_client(DATABASE_NAME)
    book_container_client = db_client.get_container_client(BOOKS_CONTAINER)
    
    # Read all items in books container
    
    for book in book_container_client.read_all_items():
        print(f'id: {book['id']} category: {book['category']} title: {book['title']}')

    # Read a single item by id
        
    print(book_container_client.read_item('b9f2e8d7-3c4a-4b1f-95e6-7a8d2f10c5e9', 'Fiction'))
    
    # Insert an item
    
    # new_book = {
    #     "id": str(uuid.uuid4()),
    #     "title": "The Seven and a Half Deaths of Evelyn Hardcastle",
    #     "author": "Stuart Turton",
    #     "category": "Mystery",
    #     "publishedDate": "2018-09-18",
    #     "description": "Aiden Bishop must solve a murder that repeats itself over eight days, inhabiting a different guest's body each day at Blackheath Manor. He must identify Evelyn Hardcastle's killer before she dies at 11:00 p.m., or the cycle will begin again.",
    #     "rating": 4.3,
    #     "tags": [
    #         "mystery",
    #         "thriller",
    #         "time loop",
    #         "psychological"
    #     ],
    #     "pageCount": 432,
    #     "isbn": "9781492657965",
    #     "imageUrl": "https://example.com/evelyn-hardcastle-cover.jpg",
    #     "embeddings": {
    #         "contentVector": [
    #             0.367,
    #             -0.892,
    #             0.445,
    #             0.678,
    #             -0.234,
    #             0.901,
    #             -0.567,
    #             0.789
    #         ],
    #         "model": "text-embedding-ada-002",
    #         "version": "1.0"
    #     },
    #     "reviews": [
    #         {
    #             "userId": "u4p5q6r7-8s9t-0u1v-2w3x-4y5z6a7b8c9d",
    #             "rating": 5,
    #             "comment": "A mind-bending murder mystery that combines Agatha Christie with Groundhog Day."
    #         }
    #     ]
    # }
    
    # book_container_client.create_item(new_book)

    # Query items to get all distinct values for tags
    
    query = "SELECT DISTINCT VALUE tag FROM c JOIN tag in c.tags"
    tags = list(book_container_client.query_items(query, enable_cross_partition_query=True))
    
    for tag in tags:
        print(f'non standard: {tag}')
        
    # Update an item
    
    # all_query = "SELECT c.id, c.category FROM c"
    # books = list(book_container_client.query_items(all_query, enable_cross_partition_query=True))
    
    # for book in books:
    #     doc = book_container_client.read_item(book['id'], book['category'])
    #     doc['tags'] = [tag.lower() for tag in doc['tags']]
    #     book_container_client.replace_item(item=doc['id'], body=doc)
    
    
    # Delete an item
    # book_container_client.delete_item('c10f84e8-5626-4075-94cb-0fe28a83d0b5',)
    
        
except Exception as e:
    print(f'There was an error: {e}')