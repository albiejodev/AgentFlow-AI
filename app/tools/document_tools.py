from app.db.chroma_db import (
    ChromaDB
)

def search_documents(
    query: str
):

    results = ChromaDB.search(query)

    print(results)

    return results
    