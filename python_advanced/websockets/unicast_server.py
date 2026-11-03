#!/usr/bin/env python3

import asyncio

import websockets


connected_clients = set()


async def connection_handler(websocket):
    connected_clients.add(websocket)

    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")
    finally:
        connected_clients.remove(websocket)


async def main():
    server = await websockets.serve(connection_handler, "127.0.0.1", 8765)
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
