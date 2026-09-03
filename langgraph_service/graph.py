import json
import os
from typing import TypedDict
from urllib.request import Request, urlopen

from langgraph.graph import StateGraph, START, END


LANGCHAIN_BASE_URL = os.getenv(
    "LANGCHAIN_BASE_URL",
    "http://langchain-service.ai-infra.svc.cluster.local:8000",
)


class AgentState(TypedDict):
    message: str


def call_langchain(message: str) -> str:
    payload = json.dumps({
        "message": message,
    }).encode("utf-8")

    request = Request(
        f"{LANGCHAIN_BASE_URL.rstrip('/')}/invoke",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urlopen(request, timeout=300) as response:
        result = json.loads(response.read().decode("utf-8"))

    return result["response"]


def process_message(state: AgentState):
    response = call_langchain(state["message"])
    return {"message": response}


builder = StateGraph(AgentState)

builder.add_node("process", process_message)

builder.add_edge(START, "process")
builder.add_edge("process", END)

graph = builder.compile()
