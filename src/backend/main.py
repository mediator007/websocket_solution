import os

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from loguru import logger
from dotenv import load_dotenv

from api import websocket_api

load_dotenv()

logger.add(
    "yadro_test_task_logger.log", 
    format="{time} {level} {message}", 
    level="INFO",
    rotation="1 MB"
    )

app = FastAPI(
    title="Yadro test task",
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)

host = os.environ.get('HOST')

origins = [
    f"http://localhost:3000",
    f"http://{host}:80"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(websocket_api.api_router, prefix='/api')