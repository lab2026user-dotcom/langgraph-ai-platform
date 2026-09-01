from typing import TypedDict

from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    message: str


def process_message(state: AgentState):
    return {
        "message": state["message"] + " -> processed by LangGraph"
    }


builder = StateGraph(AgentState)

builder.add_node("process", process_message)

builder.add_edge(START, "process")
builder.add_edge("process", END)

graph = builder.compile()
