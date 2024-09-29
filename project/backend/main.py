from collections.abc import Callable

from asgiref.sync import sync_to_async
from backend.domains.messages.routes import api_router as messages_api_router
from django.db import connections
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

app = FastAPI()


@app.middleware("http")
async def django_db(request: Request, call_next: Callable) -> Response:
    await db_connect()
    response: Response = await call_next(request)
    return response


@sync_to_async
def db_connect() -> None:
    connections["default"].connect()


@app.get("/", include_in_schema=False)
def health() -> str:
    return "OK"


app.include_router(messages_api_router, prefix="/api/messages")
