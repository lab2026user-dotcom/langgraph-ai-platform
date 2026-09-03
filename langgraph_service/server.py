from starlette.applications import Starlette
from starlette.concurrency import run_in_threadpool
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route

from langgraph_service.graph import graph


async def health(request: Request):
    return JSONResponse({
        "status": "ok",
        "service": "langgraph",
    })


async def invoke(request: Request):
    body = await request.json()

    message = body.get("message")

    if not message:
        return JSONResponse(
            {"error": "message is required"},
            status_code=400,
        )

    result = await run_in_threadpool(
        graph.invoke,
        {"message": message},
    )

    return JSONResponse(result)


routes = [
    Route("/health", health, methods=["GET"]),
    Route("/invoke", invoke, methods=["POST"]),
]


app = Starlette(
    debug=False,
    routes=routes,
)
