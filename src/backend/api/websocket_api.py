import time

from fastapi import WebSocket
from fastapi import APIRouter

from main import logger

api_router = APIRouter()

@api_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    logger.success('Websocket connection accept')
    while True:
        try:
            await websocket.receive_text()
            resp = {'timer': time.time()}
            await websocket.send_json(resp)
        except Exception as e:
            logger.error(f"Websocket error: {e}")
            break
    logger.info('Connection refused')