"""websocket.py.

An ansible-rulebook event source plugin for receiving events via a wbsocket.

Arguments:
---------
    host:               The host where the websocket is hosted. Defaults to "127.0.0.1".
    port:               The port where the websocket is listening. Defaults to "8181".
    path:               The path of the websocket. Defaults to "/core".
    protocol:           Use ws:// or wss:// protocol. Defaults to "ws".
    delay:              The delay in seconds. Defaults to 0.

Example:
-------
    - smartgic.eda.websocket:
        host: 127.0.0.1
        port: 8181
        path: /core
        protocol: ws
        delay: 0

"""

from typing import Any, Dict
import asyncio
import json
import logging
import websockets


async def main(queue: asyncio.Queue, args: Dict[str, Any]) -> str:
    """Receive events via websocket."""
    host = args.get("host", "127.0.0.1")
    port = int(args.get("port", 8181))
    path = args.get("path", "/core")
    protocol = args.get("protocol", "ws")
    delay = args.get("delay", 0)
    url = f"{protocol}://{host}:{port}{path}"

    logger = logging.getLogger()

    try:
        async for ws in websockets.connect(url):
            logger.info("Connected to websocket")
            while True:
                data = None
                try:
                    message = await ws.recv()
                    data = json.loads(message)
                except json.decoder.JSONDecodeError:
                    data = message

                if data:
                    await queue.put(data)
                await asyncio.sleep(delay)
    finally:
        logger.info("Closing websocket connection")


if __name__ == "__main__":

    class MockQueue:
        """A fake connection."""

        async def put(self: "MockQueue", event: dict) -> None:
            """Print the event."""
            print(event)  # noqa: T201

    asyncio.run(
        main(
            MockQueue(),
            {"protocol": "ws", "host": "127.0.0.1", "port": "8181", "path": "/core"},
        ),
    )
