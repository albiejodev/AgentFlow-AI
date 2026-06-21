# AgentFlow-AI Architecture

```text
                    +-------------------+
                    |      Client       |
                    |  (Web / Postman)  |
                    +---------+---------+
                              |
                              v
                    +-------------------+
                    |      FastAPI      |
                    |   /chat endpoint  |
                    +---------+---------+
                              |
                              v
                  +-----------------------+
                  |   LangGraph Workflow  |
                  +-----------+-----------+
                              |
             +----------------+----------------+
             |                                 |
             v                                 v

    +------------------+             +------------------+
    |   Memory Node    |             |   Router Node    |
    | Retrieve History |             | Route Intent     |
    +--------+---------+             +--------+---------+
             |                                |
             |                                |
             +---------------+----------------+
                             |
                             v

                  +----------------------+
                  |      Tool Node       |
                  | Execute Tool Calls   |
                  +----------+-----------+
                             |
                             v

                  +----------------------+
                  |     Answer Node      |
                  | Generate Response    |
                  +----------+-----------+
                             |
                             v

                  +----------------------+
                  |   Final Response     |
                  +----------------------+

```

## State Object

```python
AgentState:
- session_id
- question
- history
- route
- tool_result
- answer
```

## Workflow

1. User sends a question.
2. Memory Node loads session history.
3. Router Node determines intent.
4. Tool Node executes required actions.
5. Answer Node generates the final response.
6. Updated conversation state is returned.
7. Session memory is preserved for future interactions.

## Tech Stack

* Python
* FastAPI
* LangGraph
* ChromaDB
* OpenAI / Gemini
* Session Memory

```
```
