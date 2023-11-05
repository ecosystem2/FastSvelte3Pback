from typing import Optional, List
from fastapi import FastAPI, UploadFile, File, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

# routing of schema validation
from schemamodels.models.basematerialschema import validate_and_log_data as validate_and_log_base_materials
from schemamodels.models.materialschema import validate_and_log_data as validate_and_log_materials
from schemamodels.models.componentschema import validate_and_log_data as validate_and_log_components
from schemamodels.models.completepackagingschema import validate_and_log_data as validate_and_log_completepackaging
from schemamodels.models.multipackschema import validate_and_log_data as validate_and_log_multipack
from schemamodels.models.loadcatalogueschema import validate_and_log_data as validate_and_log_loadcatalogue
from schemamodels.models.loadschema import validate_and_log_data as validate_and_log_load

# routing of schema logging
from schemamodels.models.basematerialschema import read_log_file_contents as read_base_materials_log_contents
from schemamodels.models.materialschema import read_log_file_contents as read_materials_log_contents
from schemamodels.models.componentschema import read_log_file_contents as read_components_log_contents
from schemamodels.models.completepackagingschema import read_log_file_contents as read_completepackaging_log_contents
from schemamodels.models.multipackschema import read_log_file_contents as read_multipack_log_contents
from schemamodels.models.loadschema import read_log_file_contents as read_load_log_contents
from schemamodels.models.loadcatalogueschema import read_log_file_contents as read_loadcatalogue_log_contents


# uvicorn main:app --reload in terminal


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

# basematerials


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

# materials


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

# components


@app.post("/components/")
async def upload_materials(file: UploadFile):
    # Read CSV data into a pandas DataFrame
    data = pd.read_csv(file.file)

    # Validate and log errors for materials schema
    validate_and_log_components(data)

    # Read the log file contents for materials schema
    log_contents = read_components_log_contents()

    if log_contents:
        await send_log_contents_to_clients(log_contents)
        return {"message": "File uploaded with validation errors!", "log_contents": log_contents}
    else:
        return {"message": "File uploaded and validated successfully!", "log_contents": None}

# complete packaging


@app.post("/completepackaging/")
async def upload_materials(file: UploadFile):
    # Read CSV data into a pandas DataFrame
    data = pd.read_csv(file.file)

    # Validate and log errors for materials schema
    validate_and_log_completepackaging(data)

    # Read the log file contents for materials schema
    log_contents = read_completepackaging_log_contents()

    if log_contents:
        await send_log_contents_to_clients(log_contents)
        return {"message": "File uploaded with validation errors!", "log_contents": log_contents}
    else:
        return {"message": "File uploaded and validated successfully!", "log_contents": None}

# multipack


@app.post("/multipack/")
async def upload_materials(file: UploadFile):
    # Read CSV data into a pandas DataFrame
    data = pd.read_csv(file.file)

    # Validate and log errors for materials schema
    validate_and_log_multipack(data)

    # Read the log file contents for materials schema
    log_contents = read_multipack_log_contents()

    if log_contents:
        await send_log_contents_to_clients(log_contents)
        return {"message": "File uploaded with validation errors!", "log_contents": log_contents}
    else:
        return {"message": "File uploaded and validated successfully!", "log_contents": None}

# load catalogue


@app.post("/loadcatalogue/")
async def upload_materials(file: UploadFile):
    # Read CSV data into a pandas DataFrame
    data = pd.read_csv(file.file)

    # Validate and log errors for materials schema
    validate_and_log_loadcatalogue(data)

    # Read the log file contents for materials schema
    log_contents = read_loadcatalogue_log_contents()

    if log_contents:
        await send_log_contents_to_clients(log_contents)
        return {"message": "File uploaded with validation errors!", "log_contents": log_contents}
    else:
        return {"message": "File uploaded and validated successfully!", "log_contents": None}

# load


@app.post("/load/")
async def upload_materials(file: UploadFile):
    # Read CSV data into a pandas DataFrame
    data = pd.read_csv(file.file)

    # Validate and log errors for materials schema
    validate_and_log_load(data)

    # Read the log file contents for materials schema
    log_contents = read_load_log_contents()

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
