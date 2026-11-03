#!/usr/bin/env python3

import asyncio

import websockets


async def connect_and_send(uri: str, text: str) -> str:   
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
        return response


async def main():
    uri = "ws://localhost:8765"
    message = "demo"

    response = await connect_and_send(uri, message)
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
