# AgentFlow-AI

AgentFlow-AI is a production-oriented AI workflow engine built to explore the core patterns behind modern AI agents, customer support systems, AI copilots, workflow automation platforms, and AI voice assistants.

The project combines LangGraph, FastAPI, ChromaDB, session memory, tool calling, and LLM-based routing to create a modular agent capable of reasoning, retrieving information, selecting tools, and maintaining conversational context across sessions.

As AI systems become increasingly capable, I wanted to move beyond simply consuming AI tools and learn how they are actually built. AgentFlow-AI was created as a hands-on exploration of agentic workflows, memory systems, retrieval pipelines, tool orchestration, and production AI architecture.

---

# Problem Statement

Traditional applications follow deterministic workflows:

```text
Input → Business Logic → Output
```

Modern AI systems require a different architecture:

```text
Input → Memory → Reasoning → Tool Selection → Retrieval → Response
```

AgentFlow-AI was built to understand and implement these building blocks in a structured, maintainable, and extensible way.

The goal is to simulate how production AI systems operate while keeping the architecture simple enough to experiment with and extend.

---

# Key Features

## LangGraph Workflow

- State-based agent architecture
- Node and edge orchestration
- Conditional routing
- Multi-step agent execution

## LLM Integration

- OpenAI support
- Google Gemini support
- Configurable provider switching

## Memory

- Session-based conversation memory
- Context-aware responses
- Chat history persistence

## Retrieval Augmented Generation (RAG)

- ChromaDB vector database
- Semantic document retrieval
- Context injection into prompts

## Tool Calling

- Document Search Tool
- Time Tool
- Extensible tool architecture

## Intelligent Routing

- LLM-powered route selection
- Dynamic tool invocation
- Direct-answer support

## API First

- FastAPI backend
- REST endpoints
- Swagger documentation

---

# Architecture

```text
                        ┌─────────────────┐
                        │     Client      │
                        │ Web / Postman   │
                        └────────┬────────┘
                                 │
                                 ▼
                        ┌─────────────────┐
                        │     FastAPI     │
                        │  REST Endpoint  │
                        └────────┬────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │    LangGraph Engine     │
                    └────────────┬────────────┘
                                 │
          ┌──────────────────────┼──────────────────────┐
          │                      │                      │
          ▼                      ▼                      ▼

 ┌────────────────┐   ┌────────────────┐   ┌────────────────┐
 │  Memory Node   │   │  Router Node   │   │  State Store   │
 │ Session Recall │   │ Intent Detect  │   │ AgentState     │
 └────────┬───────┘   └────────┬───────┘   └────────────────┘
          │                    │
          │                    ▼
          │          ┌────────────────────┐
          │          │   Tool Selection   │
          │          └─────────┬──────────┘
          │                    │
          ▼                    ▼

 ┌────────────────┐   ┌────────────────┐
 │ Document Tool  │   │   Time Tool    │
 │   ChromaDB     │   │ System Utility │
 └────────┬───────┘   └────────┬───────┘
          │                    │
          └──────────┬─────────┘
                     ▼

            ┌──────────────────┐
            │   Answer Node    │
            │  LLM Generation  │
            └────────┬─────────┘
                     │
                     ▼

            ┌──────────────────┐
            │ Memory Update    │
            └────────┬─────────┘
                     │
                     ▼

            ┌──────────────────┐
            │ Final Response   │
            └──────────────────┘
```

---

# Design Decisions

## Why LangGraph?

LangGraph provides explicit state management and workflow orchestration, making agent behavior deterministic and easier to debug compared to prompt-only approaches.

## Why FastAPI?

FastAPI offers strong typing, high performance, and straightforward API development, making it ideal for serving AI workloads.

## Why ChromaDB?

ChromaDB provides lightweight semantic retrieval capabilities while keeping local development and experimentation simple.

## Why Session Memory?

Session memory enables conversational continuity while keeping the architecture lightweight. A production deployment would likely use Redis or a dedicated persistence layer.

---

# Challenges & Learnings

## Routing vs Tool Execution

One early design decision was whether routing and tool execution should be combined into a single node. As the workflow evolved, separating these concerns improved maintainability and made the graph easier to extend.

## Memory Management

Passing excessive conversation history increased latency and token consumption. This led to a more selective memory strategy focused on preserving only relevant context.

## Balancing Determinism and LLM Reasoning

Reliable AI systems often require a combination of deterministic workflows and probabilistic LLM reasoning. Finding the right balance was one of the key lessons from building this project.

---

# Tech Stack

## Backend

- FastAPI
- Python 3.12

## Agent Framework

- LangGraph

## LLMs

- OpenAI
- Google Gemini

## Vector Database

- ChromaDB

## Environment Management

- python-dotenv

---

# Project Structure

```text
AgentFlow-AI
│
├── app
│   ├── agents
│   ├── api
│   ├── db
│   ├── services
│   ├── tools
│   ├── config.py
│   └── main.py
│
├── chroma_data
├── scripts
├── requirements.txt
├── .env.example
└── README.md
```

---

# Installation

```bash
git clone https://github.com/your-username/AgentFlow-AI.git

cd AgentFlow-AI

python -m venv env

# Windows
env\Scripts\activate

# Linux / Mac
source env/bin/activate

pip install -r requirements.txt
```

---

# Environment Variables

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

Request:

```http
GET /chat?session_id=albin&question=My name is Albin
```

Follow-up:

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

# Current Capabilities

- Conversation Memory
- LLM Routing
- Tool Calling
- RAG Workflows
- ChromaDB Retrieval
- Multi-Step Agent Execution

---

# Future Roadmap

## Completed

- LangGraph Workflow
- Tool Calling
- ChromaDB Integration
- Conversation Memory
- LLM Routing

## Planned

- Redis Memory Persistence
- Streaming Responses
- Web Search Tool
- CRM Integration
- Human Handoff
- Voice Agent Integration
- Multi-Agent Workflows

---

# Learning Outcomes

This project explores:

- Agentic Workflows
- Retrieval Augmented Generation (RAG)
- Tool Calling
- Session Memory
- LLM Routing
- Vector Databases
- Multi-Step Reasoning
- AI System Design
- Production AI Architecture

---

# License

MIT License
