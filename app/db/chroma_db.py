import chromadb


class ChromaDB:

    client = chromadb.PersistentClient(
        path="chroma_data"
    )

    collection = client.get_or_create_collection(
        name="documents"
    )

    @classmethod
    def search(
        cls,
        query: str,
        top_k: int = 3
    ):

        results = cls.collection.query(
            query_texts=[query],
            n_results=top_k
        )

        return results