#!/usr/bin/env python3

import asyncio

import websockets
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    try:
        async for message in websocket:
            if len(message.strip()) == 0:
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send(f"OK:{message}")
    except ConnectionClosed:
        pass


async def main():
    server = await websockets.serve(connection_handler, "127.0.0.1", 8765)
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
