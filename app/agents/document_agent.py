from typing import TypedDict
from langgraph.graph import StateGraph
from app.services.llm_service import (
    LLMService
)
import logging
from app.tools.time_tools import (get_current_time)
from app.tools.document_tools import (search_documents)
from app.services.llm_service import (
    LLMService
)

logger  = logging.getLogger(__name__)


class AgentState(TypedDict):

        question : str
        context : str 
        answer : str
        route : str
        tool_result : any



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

    tool_result = state["tool_result"]

    if isinstance(tool_result, str):

        context = tool_result

    else:

        context = "\n".join(
            item["text"]
            for item in tool_result
        )

    prompt = f"""
    You are a helpful AI assistant.

    Answer the user's question
    using only the provided context.

    Context:

    {context}

    Question:

    {state["question"]}
    """

    answer = LLMService.generate(
        prompt
    )

    state["answer"] = answer

    return state




#conditional route node 3 
def router_node(
    state: AgentState
):

    question = (
        state["question"]
        .lower()
    )

    if "time" in question:

        state["route"] = "time"

    else:

        state["route"] = "document"

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

graph_builder.add_conditional_edges(
    "router",
    route_decision,
    {
        "time": "tool",
        "document": "tool"
    }
)

graph_builder.add_edge(
    "tool",
    "answer"
)

graph_builder.set_entry_point(
    "router"
)

agent = graph_builder.compile()