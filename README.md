# AgentFlow-AI

A LangGraph-powered AI Agent built with FastAPI, ChromaDB, Memory Management, Tool Calling, and LLM Routing.

AgentFlow-AI demonstrates the core building blocks used in modern AI assistants, AI copilots, AI customer support agents, and AI voice receptionists.

---

## Features

### LangGraph Workflow

* State-based agent architecture
* Node and edge orchestration
* Conditional routing
* Multi-step agent execution

### LLM Integration

* Gemini support
* OpenAI support
* Configurable provider via environment variables

### Memory

* Session-based conversation memory
* Chat history persistence
* Context-aware responses

### Retrieval Augmented Generation (RAG)

* ChromaDB vector database
* Semantic document retrieval
* Context injection into LLM prompts

### Tool Calling

* Document Search Tool
* Time Tool
* Extensible tool architecture

### Intelligent Routing

* LLM-powered route selection
* Dynamic tool choice
* Direct answer support

### API First

* FastAPI backend
* REST endpoints
* Swagger documentation

---

# Architecture

```text
User Question
      │
      ▼
 Memory Node
      │
      ▼
 LLM Router
      │
      ├─────────────┬──────────────┐
      ▼             ▼              ▼
 Time Tool    Document Tool    Direct Answer
      │             │
      └──────┬──────┘
             ▼
        Answer Node
             │
             ▼
      Save Memory
             │
             ▼
          Response
```

---

# Tech Stack

## Backend

* FastAPI
* Python 3.12

## Agent Framework

* LangGraph

## LLMs

* OpenAI
* Google Gemini

## Vector Database

* ChromaDB

## Environment Management

* python-dotenv

---

# Project Structure

```text
AgentFlow-AI
│
├── app
│   ├── agents
│   │   └── document_agent.py
│   │
│   ├── api
│   │   └── agent.py
│   │
│   ├── db
│   │   └── chroma_db.py
│   │
│   ├── services
│   │   ├── agent_service.py
│   │   ├── memory_service.py
│   │   ├── llm_service.py
│   │   ├── openai_service.py
│   │   └── gemini_service.py
│   │
│   ├── tools
│   │   ├── document_tool.py
│   │   └── time_tool.py
│   │
│   ├── config.py
│   └── main.py
│
├── chroma_data
├── scripts
│   └── load_test_data.py
│
├── .env
├── .env.example
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/your-username/AgentFlow-AI.git

cd AgentFlow-AI
```

Create virtual environment:

```bash
python -m venv env
```

Activate environment:

Windows:

```bash
env\Scripts\activate
```

Linux/Mac:

```bash
source env/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
LLM_PROVIDER=gemini

OPENAI_API_KEY=your_openai_key
OPENAI_MODEL=gpt-4.1-mini

GOOGLE_API_KEY=your_google_api_key
GEMINI_MODEL=gemini-2.5-flash
```

---

# Run Application

```bash
python -m uvicorn app.main:app --reload
```

Application:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

---

# Load Sample Documents

```bash
python -m scripts.load_test_data
```

---

# Example API Calls

## Ask Agent

```http
GET /chat?session_id=test-user&question=What is Python?
```

Response:

```json
{
  "answer": "Python is a high-level programming language..."
}
```

---

## Memory Example

Request 1:

```http
GET /chat?session_id=albin&question=My name is Albin
```

Request 2:

```http
GET /chat?session_id=albin&question=What is my name?
```

Response:

```json
{
  "answer": "Your name is Albin."
}
```

---

# Supported Routes

| Route    | Purpose                    |
| -------- | -------------------------- |
| time     | Time related queries       |
| document | Document retrieval queries |
| direct   | Direct LLM answers         |

---

# Future Roadmap

### Completed

* LangGraph Workflow
* Tool Calling
* ChromaDB Integration
* Conversation Memory
* LLM Routing
* Multi Tool Support

### Planned

* Redis Memory Persistence
* Streaming Responses
* Web Search Tool
* Calendar Tool
* CRM Integration
* Human Handoff
* Voice Agent Integration

---

# Learning Outcomes

This project demonstrates:

* Agentic Workflows
* Retrieval Augmented Generation (RAG)
* Tool Calling
* Vector Databases
* Session Memory
* LLM Routing
* Multi-Step Reasoning
* FastAPI Development
* AI System Design

---

# License

MIT License
