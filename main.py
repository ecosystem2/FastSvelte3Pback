from typing import Optional, List
from fastapi import FastAPI, UploadFile, File, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from schemamodels.models.basematerialschema import validate_and_log_data as validate_and_log_base_materials
from schemamodels.models.materialschema import validate_and_log_data as validate_and_log_materials
from schemamodels.models.basematerialschema import read_log_file_contents as read_base_materials_log_contents
from schemamodels.models.materialschema import read_log_file_contents as read_materials_log_contents
import pandas as pd

app = FastAPI()

# uvicorn main:app --reload in terminal


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/basematerials/")
async def upload_base_materials(file: UploadFile):
    # Read CSV data into a pandas DataFrame
    data = pd.read_csv(file.file)

    # Validate and log errors for base materials schema
    validate_and_log_base_materials(data)

    # Read the log file contents for base materials schema
    log_contents = read_base_materials_log_contents()

    if log_contents:
        await send_log_contents_to_clients(log_contents)
        return {"message": "File uploaded with validation errors!", "log_contents": log_contents}
    else:
        return {"message": "File uploaded and validated successfully!", "log_contents": None}


@app.post("/materials/")
async def upload_materials(file: UploadFile):
    # Read CSV data into a pandas DataFrame
    data = pd.read_csv(file.file)

    # Validate and log errors for materials schema
    validate_and_log_materials(data)

    # Read the log file contents for materials schema
    log_contents = read_materials_log_contents()

    if log_contents:
        await send_log_contents_to_clients(log_contents)
        return {"message": "File uploaded with validation errors!", "log_contents": log_contents}
    else:
        return {"message": "File uploaded and validated successfully!", "log_contents": None}


@app.get("/logfile/")
async def get_log_file():
    # Replace with the actual path to your log file
    log_path = "validation_errors.log"
    return FileResponse(log_path)

origins = [
    "http://localhost:5173",
    "localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

websocket_connections = []


async def send_log_contents_to_clients(log_contents):
    for connection in websocket_connections:
        await connection.send_text(log_contents)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    websocket_connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Handle any incoming messages if necessary
    except WebSocketDisconnect:
        websocket_connections.remove(websocket)
