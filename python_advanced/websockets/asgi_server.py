#!/usr/bin/env python3

from pathlib import Path

from starlette.applications import Starlette
from starlette.responses import FileResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect


BASE_DIR = Path(__file__).resolve().parent


async def homepage(request):
    return FileResponse(BASE_DIR / "index.html")


async def stylesheet(request):
    return FileResponse(BASE_DIR / "style.css", media_type="text/css")


async def javascript(request):
    return FileResponse(BASE_DIR / "chat.js", media_type="text/javascript")


async def websocket_endpoint(websocket):
    await websocket.accept()

    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except WebSocketDisconnect:
        pass


app = Starlette(
    routes=[
        Route("/", homepage),
        Route("/style.css", stylesheet),
        Route("/chat.js", javascript),
        WebSocketRoute("/ws", websocket_endpoint),
    ]
)
