from app.db.chroma_db import ChromaDB

try:
    ChromaDB.collection.delete(
        ids=["1"]
    )
except:
    pass

ChromaDB.collection.add(
    ids=["1"],
    documents=[
        """
        Albin has experience with
        RabbitMQ,
        Microservices,
        FastAPI,
        MongoDB
        """
    ]
)

print("Test data inserted")