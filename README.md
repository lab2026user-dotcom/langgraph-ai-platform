# On-Prem LangGraph Service

Standalone on-prem LangGraph service using the official open-source LangGraph core with a thin Starlette HTTP adapter.

## Architecture

Existing FastAPI -> LangGraph Service -> LangGraph Core

## Endpoints

GET /health
POST /invoke

## Source

Official LangGraph source is included under libs/langgraph.
Source commit: 11ee185999b86bfea2d8c0e69cef9a5e37acf686

## Runtime

Python 3.11, Starlette, and Uvicorn.

The service does not directly install langgraph-api, langgraph-runtime-inmem, langchain, or langchain-ollama.

Container builds use Argo Workflows, Kaniko, and Harbor.
