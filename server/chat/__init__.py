import json

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from datetime import datetime
from .connection_manager import ConnectionManager
from ..database import Database
from ..models.message import Message, EditMessage

baseApi = "/api/v1"
router = APIRouter(prefix=baseApi + "/chats")
db = Database()
manager = ConnectionManager()


@router.websocket("/all/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    try:
        while True:
            jsonData = await websocket.receive_text()
            username = json.loads(jsonData)["username"]
            mes = json.loads(jsonData)["message"]
            message = {"time": current_time,
                       "clientId": client_id,
                       "username": username,
                       "message": mes}
            db.addChat(username, mes)
            await manager.broadcast(json.dumps(message))

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        message = {"time": current_time, "clientId": client_id, "message": "Offline"}
        await manager.broadcast(json.dumps(message))


@router.post("/edit")
async def editMessage(editMes: EditMessage):
    return db.editMessage(editMes)


@router.delete("/{messageID}")
async def deleteMessage(messageID):
    return db.deleteMessage(messageID)


@router.get("/all")
async def getCurrentChat():
    return db.getAllChats()
