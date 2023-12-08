from typing import Optional, List
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd


# routing of schema validation
from schemamodels.models.basematerialschema import validateAndLog as validate_and_log_base_materials
from schemamodels.models.materialschema import validateAndLog as validate_and_log_materials
from schemamodels.models.componentschema import validateAndLog as validate_and_log_components
from schemamodels.models.completepackagingschema import validateAndLog as validate_and_log_completepackaging
from schemamodels.models.multipackschema import validateAndLog as validate_and_log_multipack
from schemamodels.models.loadcatalogueschema import validateAndLog as validate_and_log_loadcatalogue
from schemamodels.models.loadschema import validateAndLog as validate_and_log_load


# launching the app in terminal type:
# uvicorn main:app --reload


app = FastAPI()

# file routing


async def read_file(file: UploadFile):
    # Determine the file extension
    file_extension = file.filename.split(".")[-1]

    # Read the file based on its extension
    if file_extension == "csv":
        return pd.read_csv(file.file)
    elif file_extension == "json":
        return pd.read_json(file.file)
    elif file_extension == "xlsx":
        return pd.read_excel(file.file)
    else:
        raise ValueError("Unsupported file format")

# basematerials


@app.post("/basematerials/")
async def upload_base_materials(file: UploadFile = File(...)):
    try:
        # Read data into a pandas DataFrame
        data = await read_file(file)

        # Perform schema validation based on the file type
        if file.filename.endswith(".csv"):
            validation_response = validate_and_log_base_materials(data)
        elif file.filename.endswith(".json"):
            # Adjust based on the actual validation function for JSON
            validation_response = validate_and_log_base_materials(data)
        elif file.filename.endswith(".xlsx"):
            # Adjust based on the actual validation function for Excel
            validation_response = validate_and_log_base_materials(data)
        else:
            raise ValueError("Unsupported file format")

        # Check if any logs have been produced
        if validation_response:
            # Check if validation_response is an empty array
            if validation_response == "[]":
                return {"message": "File uploaded and validated successfully!", "log_contents": "Your data appears to be Open 3P compliant!"}
            else:
                return {"message": "File uploaded with validation errors!", "log_contents": validation_response}
        else:
            return {"message": "File uploaded and validated successfully!", "log_contents": None}
    except Exception as e:
        return {"message": f"Error processing file: {str(e)}"}

# materials


@app.post("/materials")
async def upload_materials(file: UploadFile = File(...)):
    try:
        # Read data into a pandas DataFrame
        data = await read_file(file)

        # Perform schema validation based on the file type
        if file.filename.endswith(".csv"):
            validation_response = validate_and_log_materials(data)
        elif file.filename.endswith(".json"):
            # Adjust based on the actual validation function for JSON
            validation_response = validate_and_log_materials(data)
        elif file.filename.endswith(".xlsx"):
            # Adjust based on the actual validation function for Excel
            validation_response = validate_and_log_materials(data)
        else:
            raise ValueError("Unsupported file format")

       # Check if any logs have been produced
        if validation_response:
            # Check if validation_response is an empty array
            if validation_response == "[]":
                return {"message": "File uploaded and validated successfully!", "log_contents": "Your data appears to be Open 3P compliant!"}
            else:
                return {"message": "File uploaded with validation errors!", "log_contents": validation_response}
        else:
            return {"message": "File uploaded and validated successfully!", "log_contents": None}
    except Exception as e:
        return {"message": f"Error processing file: {str(e)}"}


# Components
@app.post("/components/")
async def upload_components(file: UploadFile = File(...)):
    try:
        # Read data into a pandas DataFrame
        data = await read_file(file)

        # Perform schema validation based on the file type
        if file.filename.endswith(".csv"):
            validation_response = validate_and_log_components(data)
        elif file.filename.endswith(".json"):
            # Adjust based on the actual validation function for JSON
            validation_response = validate_and_log_components(data)
        elif file.filename.endswith(".xlsx"):
            # Adjust based on the actual validation function for Excel
            validation_response = validate_and_log_components(data)
        else:
            raise ValueError("Unsupported file format")

       # Check if any logs have been produced
        if validation_response:
            # Check if validation_response is an empty array
            if validation_response == "[]":
                return {"message": "File uploaded and validated successfully!", "log_contents": "Your data appears to be Open 3P compliant!"}
            else:
                return {"message": "File uploaded with validation errors!", "log_contents": validation_response}
        else:
            return {"message": "File uploaded and validated successfully!", "log_contents": None}
    except Exception as e:
        return {"message": f"Error processing file: {str(e)}"}

# Complete Packaging


@app.post("/completepackaging/")
async def upload_complete_packaging(file: UploadFile = File(...)):
    try:
        # Read data into a pandas DataFrame
        data = await read_file(file)

        # Perform schema validation based on the file type
        if file.filename.endswith(".csv"):
            validation_response = validate_and_log_completepackaging(data)
        elif file.filename.endswith(".json"):
            # Adjust based on the actual validation function for JSON
            validation_response = validate_and_log_completepackaging(data)
        elif file.filename.endswith(".xlsx"):
            # Adjust based on the actual validation function for Excel
            validation_response = validate_and_log_completepackaging(data)
        else:
            raise ValueError("Unsupported file format")

        # Check if any logs have been produced
        if validation_response:
            # Check if validation_response is an empty array
            if validation_response == "[]":
                return {"message": "File uploaded and validated successfully!", "log_contents": "Your data appears to be Open 3P compliant!"}
            else:
                return {"message": "File uploaded with validation errors!", "log_contents": validation_response}
        else:
            return {"message": "File uploaded and validated successfully!", "log_contents": None}
    except Exception as e:
        return {"message": f"Error processing file: {str(e)}"}

# Multipack


@app.post("/multipack/")
async def upload_multipack(file: UploadFile = File(...)):
    try:
        # Read data into a pandas DataFrame
        data = await read_file(file)

        # Perform schema validation based on the file type
        if file.filename.endswith(".csv"):
            validation_response = validate_and_log_multipack(data)
        elif file.filename.endswith(".json"):
            # Adjust based on the actual validation function for JSON
            validation_response = validate_and_log_multipack(data)
        elif file.filename.endswith(".xlsx"):
            # Adjust based on the actual validation function for Excel
            validation_response = validate_and_log_multipack(data)
        else:
            raise ValueError("Unsupported file format")

         # Check if any logs have been produced
        if validation_response:
            # Check if validation_response is an empty array
            if validation_response == "[]":
                return {"message": "File uploaded and validated successfully!", "log_contents": "Your data appears to be Open 3P compliant!"}
            else:
                return {"message": "File uploaded with validation errors!", "log_contents": validation_response}
        else:
            return {"message": "File uploaded and validated successfully!", "log_contents": None}
    except Exception as e:
        return {"message": f"Error processing file: {str(e)}"}

# Load Catalogue


@app.post("/loadcatalogue/")
async def upload_load_catalogue(file: UploadFile = File(...)):
    try:
        # Read data into a pandas DataFrame
        data = await read_file(file)

        # Perform schema validation based on the file type
        if file.filename.endswith(".csv"):
            validation_response = validate_and_log_loadcatalogue(data)
        elif file.filename.endswith(".json"):
            # Adjust based on the actual validation function for JSON
            validation_response = validate_and_log_loadcatalogue(data)
        elif file.filename.endswith(".xlsx"):
            # Adjust based on the actual validation function for Excel
            validation_response = validate_and_log_loadcatalogue(data)
        else:
            raise ValueError("Unsupported file format")

        # Check if any logs have been produced
        if validation_response:
            # Check if validation_response is an empty array
            if validation_response == "[]":
                return {"message": "File uploaded and validated successfully!", "log_contents": "Your data appears to be Open 3P compliant!"}
            else:
                return {"message": "File uploaded with validation errors!", "log_contents": validation_response}
        else:
            return {"message": "File uploaded and validated successfully!", "log_contents": None}
    except Exception as e:
        return {"message": f"Error processing file: {str(e)}"}
# Load


@app.post("/load/")
async def upload_load(file: UploadFile = File(...)):
    try:
        # Read data into a pandas DataFrame
        data = await read_file(file)

        # Perform schema validation based on the file type
        if file.filename.endswith(".csv"):
            validation_response = validate_and_log_load(data)
        elif file.filename.endswith(".json"):
            # Adjust based on the actual validation function for JSON
            validation_response = validate_and_log_load(data)
        elif file.filename.endswith(".xlsx"):
            # Adjust based on the actual validation function for Excel
            validation_response = validate_and_log_load(data)
        else:
            raise ValueError("Unsupported file format")

         # Check if any logs have been produced
        if validation_response:
            # Check if validation_response is an empty array
            if validation_response == "[]":
                return {"message": "File uploaded and validated successfully!", "log_contents": "Your data appears to be Open 3P compliant!"}
            else:
                return {"message": "File uploaded with validation errors!", "log_contents": validation_response}
        else:
            return {"message": "File uploaded and validated successfully!", "log_contents": None}
    except Exception as e:
        return {"message": f"Error processing file: {str(e)}"}


origins = [
    "open3p.ecosystem2.co.uk"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
