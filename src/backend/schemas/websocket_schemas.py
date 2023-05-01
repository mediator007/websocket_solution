from pydantic import BaseModel


class WebsocketInput(BaseModel):
    ws_need_timer: str