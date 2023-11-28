<p align="center"><img src="https://github.com/E2-RJ/Assets_ecosystem2/blob/main/Full_Logo/e2_full_logo_navy.svg" /></p>

API microservice, using Python and FastAPI, for testing files against industry schemas.

## Development Instructions

Clone this repo and install [Python](https://www.python.org/downloads/).  From the root directory of this repo, run:

```python
python -m venv ./venv #Create your python virtual environment

#WINDOWS
venv\Scripts\activate.bat
#LINUX
. venv/bin/activate

pip install --no-cache-dir --upgrade -r requirements.txt #Install project dependancies 
``` 

cd into the root directory with main.py

```python
uvicorn main:app --reload #Start the Fast API server
```

Typically hosted at `http://localhost:8000`.

| Screenshot                                                            | Description|
|-----------------------------------------------------------------------|------------|
| ![](Demonstration/Demonstration.GIF)        | Current state of the webapp. |

##TODO
- Upload Working example
- Upload Demonstartion video & GIF
- Share with collaborator

## Contributions

Pull requests are appreciated!  Please use the same [Contributor License Agreement (CLA)](https://github.com/AnalyticalGraphicsInc/cesium/blob/master/CONTRIBUTING.md) and [Coding Guide](https://github.com/AnalyticalGraphicsInc/cesium/blob/master/Documentation/Contributors/CodingGuide/README.md) used for [Cesium](http://cesiumjs.org/).
