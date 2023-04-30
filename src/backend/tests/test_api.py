import time

import pytest
from fastapi.websockets import WebSocket
from fastapi.testclient import TestClient

from main import app


def test_websocket():
    client = TestClient(app)
    with client.websocket_connect("/api/ws") as websocket:
        websocket.send_json({"msg": "Hello WebSocket"})
        data = websocket.receive_json()
        current_time = time.time()
        assert current_time - 1 <= float(data['timer']) <= current_time + 1
