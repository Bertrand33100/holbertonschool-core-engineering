#!/usr/bin/env python3
"""Petit serveur WebSocket qui renvoie les messages reçus."""

import asyncio

import websockets


async def connection_handler(websocket):
    async for message in websocket:
        await websocket.send(message)


async def main():
    server = await websockets.serve(connection_handler, "127.0.0.1", 8765)
    print("Serveur démarré sur ws://127.0.0.1:8765")

    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
