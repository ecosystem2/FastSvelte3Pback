<p align="center"><img src="https://github.com/E2-RJ/Assets_ecosystem2/blob/main/Full_Logo/e2_full_logo_navy.svg" /></p>

API microservice, using Python, Pandara and FastAPI, for testing files against industry schemas.

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

## Production Instructions

A docker file and github workflow is included within this repository. When a release is created, the docker container is built and submitted to dockerhub.

### Seting up dockerhub access token

### Setting up dockerhub credentials
- Below the repository name, in the top left corner of the screen, there is a navigation bar; **Select Settings**
- You should be presented with a page consisting with a sidbar and the repositories settings, **Select Secrets and variables**
- With the sub-section expanded, **Select Actions**
- This section **should already have two repository secrets, DOCKER_USERNAME and DOCKER_PASSWORD**
- **If this is not the case, please add them**

### Building docker container

| Screenshot                                                            | Description|
|-----------------------------------------------------------------------|------------|
| ![](Demonstration/Demonstration.GIF)        | Current state of the webapp. |

##TODO
- Upload Working example
- Upload Demonstartion video & GIF
- Share with collaborator

## Contributions

Pull requests are appreciated!  Please use the same [Contributor License Agreement (CLA)](https://github.com/AnalyticalGraphicsInc/cesium/blob/master/CONTRIBUTING.md) and [Coding Guide](https://github.com/AnalyticalGraphicsInc/cesium/blob/master/Documentation/Contributors/CodingGuide/README.md) used for [Cesium](http://cesiumjs.org/).
