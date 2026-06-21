documents = [
    {
        "text": "I worked with RabbitMQ and microservices."
    },
    {
        "text": "I built APIs using FastAPI."
    },
    {
        "text": "I used MongoDB."
    }
]




class VectorStore:

    @staticmethod
    def search(
        query: str
    ):

        return documents[:2]