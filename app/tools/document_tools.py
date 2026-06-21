from app.db.chroma_db import (
    chromaDB
)

def search_documents(
    query: str
):

    return ChromaDB.search(query)