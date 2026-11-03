#!/usr/bin/env python3

import asyncio

import websockets
from websockets.exceptions import ConnectionClosed


connected_clients = set()


async def connection_handler(websocket):
    connected_clients.add(websocket)

    try:
        async for message in websocket:
            response = f"B:{message}"

            for client in connected_clients.copy():
                try:
                    await client.send(response)
                except ConnectionClosed:
                    connected_clients.discard(client)
    finally:
        connected_clients.discard(websocket)


async def main():
    server = await websockets.serve(connection_handler, "127.0.0.1", 8765)
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
