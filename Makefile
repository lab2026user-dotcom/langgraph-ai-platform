.PHONY: help install run test lint

help:
	@echo 'Targets:'
	@echo '  install   Install runtime dependencies'
	@echo '  run       Start the LangGraph HTTP service'
	@echo '  test      Run a LangGraph smoke test'
	@echo '  lint      Run basic Python syntax checks'

install:
	python -m pip install -e .

run:
	python -m uvicorn langgraph_service.server:app --host 0.0.0.0 --port 8000

test:
	python -c "from langgraph_service.graph import graph; result = graph.invoke({'message':'test'}); assert result['message'] == 'test -> processed by LangGraph'; print('LangGraph smoke test passed')"

lint:
	python -m compileall -q langgraph_service
