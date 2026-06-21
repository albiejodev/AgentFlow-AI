from typing import TypedDict
from langgraph.graph import StateGraph
from app.services.llm_service import (
    LLMService
)
import logging
from app.tools.calculator_tool import calculate
from app.tools.time_tools import (get_current_time)
from app.tools.document_tools import (search_documents)
from app.services.llm_service import (
    LLMService
)
from app.services.memory_service import (MemoryService)

logger  = logging.getLogger(__name__)


class AgentState(TypedDict):

        question : str
        context : str 
        answer : str
        route : str
        tool_result : any
        session_id:str
        history:str



#node 1
def retrieve_node(
        state:AgentState
    ):

        logger.info("Running retrieve node")

        question = state["question"]

        state["context"]=(
            f"Retrieved context for: {question}"
        )

        return state




#node 2
def answer_node(
    state: AgentState
):

    tool_result = state.get.get("tool_result")

    if not tool_result:
        context = ""

    elif isinstance(tool_result, str):

        context = tool_result

    else:

        documents = (
            tool_result["documents"][0]
        )

        print("documents retrieved",len(documents))

        context = "\n".join(
            documents
        )

    prompt = f"""
    You are a helpful AI assistant.

    Use the conversation history
    and document context when available.

    If the answer exists in the conversation history, use it.

    If the answer exists in the document context, use it.

    If neither contains the answer,say you donot know.

    Conversation History:

    {state["history"]}

    Context:

    {context}

    Question:

    {state["question"]}
    """

    answer = LLMService.generate(
        prompt
    )

    state["answer"] = answer

    MemoryService.add_message(
    state["session_id"],
    "user",
    state["question"]
    )

    MemoryService.add_message(
        state["session_id"],
        "assistant",
        answer
    )

    return state




#conditional route node 3 
def router_node(
    state: AgentState
):

    question = state["question"]

    prompt = f"""
    You are a routing agent.

    Decide which route to use.

    Available routes:

    time
    document
    calculator
    direct

    Return ONLY one word.

    Question:

    {question}
    """

    route = (
        LLMService.generate(
            prompt
        )
        .strip()
        .lower()
    )

    state["route"] = route

    return state


#node 4
def route_decision(
    state: AgentState
):

    return state["route"]



#tool node 5
def tool_node(
    state : AgentState
):
 
    route = state["route"]
    question = state["question"]

    print("TOOL NODE EXECUTED")
    print("ROUTE =", route)


    if route == "time":
        state["tool_result"]=(
            #get_current_time()
            "Test Tool"
        )

    elif route == "document":
        state["tool_result"] = (
            search_documents(question)
        )
    elif route == "calculator":
        state["tool_result"]=(
            calculate(question)
        )
    return state




def memory_node(
    state: AgentState
):

    history = MemoryService.get_history(
        state["session_id"]
    )

    history_text = ""

    for message in history:

        history_text += (
            f"{message['role']}: "
            f"{message['content']}\n"
        )

    state["history"] = (
        history_text
    )

    return state



graph_builder = StateGraph(
    AgentState
)

graph_builder.add_node(
    "router",
    router_node
)

graph_builder.add_node(
    "tool",
    tool_node
)

graph_builder.add_node(
    "answer",
    answer_node
)

graph_builder.add_node(
    "memory",
     memory_node
)

graph_builder.add_conditional_edges(
    "router",
    route_decision,
    {
        "time": "tool",
        "document": "tool",
        "direct":"answer"
    }
)

graph_builder.add_edge(
    "tool",
    "answer"
)

graph_builder.add_edge(
    "memory",
    "router"
)

graph_builder.set_entry_point(
    "memory"
)

agent = graph_builder.compile()