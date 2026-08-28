"""On-prem LangGraph agent using the existing Ollama gateway."""

from __future__ import annotations

import os

from langchain.agents import create_agent
from langchain_ollama import ChatOllama

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://ollama-gateway.ai-lab.svc.cluster.local:11434",
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "qwen3:14b",
)

model = ChatOllama(
    model=OLLAMA_MODEL,
    base_url=OLLAMA_BASE_URL,
    temperature=0.7,
)

graph = create_agent(
    model=model,
    tools=[],
    system_prompt=(
        "You are the AI orchestration agent for an enterprise AI platform. "
        "Answer clearly and concisely. "
        "Do not claim to have performed actions that you did not perform."
    ),
    name="ai_platform_agent",
)
