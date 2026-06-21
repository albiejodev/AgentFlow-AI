class MemoryService:

    memory = {}

    @classmethod
    def get_history(
        cls,
        session_id: str
    ):

        return cls.memory.get(
            session_id,
            []
        )

    @classmethod
    def add_message(
        cls,
        session_id: str,
        role: str,
        content: str
    ):

        if session_id not in cls.memory:

            cls.memory[
                session_id
            ] = []

        cls.memory[
            session_id
        ].append(
            {
                "role": role,
                "content": content
            }
        )