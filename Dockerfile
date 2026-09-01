FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Copy official LangGraph source
COPY libs/langgraph /src/langgraph

# Install LangGraph and HTTP runtime
RUN pip install --no-cache-dir \
    /src/langgraph \
    "starlette>=0.46.0" \
    "uvicorn>=0.34.0"

# Copy standalone LangGraph service
COPY langgraph_service /app/langgraph_service

EXPOSE 8000

CMD ["uvicorn", "langgraph_service.server:app", "--host", "0.0.0.0", "--port", "8000"]
