from langgraph.graph import StateGraph
from langgraph.graph import START, END

from backend.graph.state import GraphState
from backend.graph.router import route_question

from backend.agents.datasheet_agent import datasheet_agent
from backend.agents.troubleshooting_agent import troubleshooting_agent
from backend.agents.knowledge_agent import knowledge_agent
from backend.agents.code_review_agent import code_review_agent

def router_node(state):

    state["route"] = route_question(
        state["question"]
    )

    return state


def datasheet_node(state):

    state["response"] = datasheet_agent(
        question=state["question"],
        user_id=state["user_id"],
        session_id=state["session_id"]
    )

    return state


def troubleshooting_node(state):

    state["response"] = troubleshooting_agent(
        question=state["question"],
        session_id=state["session_id"]
    )

    return state


def knowledge_node(state):

    state["response"] = knowledge_agent(
        question=state["question"],
        user_id=state["user_id"],
        session_id=state["session_id"]
    )

    return state

def code_review_node(state):

    state["response"] = code_review_agent(
        message=state["question"],
        session_id=state["session_id"]
    )

    return state


graph = StateGraph(GraphState)

graph.add_node("router", router_node)

graph.add_node("datasheet", datasheet_node)

graph.add_node("troubleshooting", troubleshooting_node)

graph.add_node("knowledge", knowledge_node)

graph.add_node("code_review",code_review_node)

graph.add_edge(START, "router")

graph.add_conditional_edges(
    "router",
    lambda state: state["route"],
    {
        "datasheet": "datasheet",
        "troubleshooting": "troubleshooting",
        "knowledge": "knowledge",
        "code_review": "code_review"
    }
)

graph.add_edge("datasheet", END)
graph.add_edge("troubleshooting", END)
graph.add_edge("knowledge", END)
graph.add_edge("code_review",END)
app_graph = graph.compile()