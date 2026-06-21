import chromadb


client = chromadb.PersistentClient(
    path="chroma_data"
)


collection = client.get_or_create_collection(
    name="documents"
)


class chromaDB:


    @staticmethod
    def search(
        query: str
    ):
        return collection.query(
            query_texts=[query],
            n_results=3
        )