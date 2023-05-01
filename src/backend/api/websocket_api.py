import time
import json

from fastapi import WebSocket, HTTPException
from fastapi import APIRouter

from main import logger
from schemas import websocket_schemas

api_router = APIRouter()


@api_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    logger.success('Websocket connection accept')
    while True:
        try:
            recieve_text = await websocket.receive_text()
            recieve_object= json.loads(recieve_text)
            try:
                websocket_schemas.WebsocketInput(**recieve_object)
            except ValueError:
                logger.error('Bad ws message')
                raise HTTPException(
                    status_code=400, detail='Bad ws message'
                    )
            resp = {'timer': time.time()}
            await websocket.send_json(resp)
        except Exception as e:
            logger.error(f"Websocket error: {e}")
            break
    logger.info('Connection refused')