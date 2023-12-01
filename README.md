<p align="center"><img src="https://github.com/E2-RJ/Assets_ecosystem2/blob/main/Full_Logo/e2_full_logo_navy.svg" /></p>

API microservice, using Python and FastAPI, for testing files against industry schemas. Data validation uses Pandera.

## Development Instructions

Clone this repo and install [Node.js](http://nodejs.org/).  From the root directory of this repo, run:

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

Typically hosted at `http://localhost:5173`.

| Screenshot                                                            | Description|
|-----------------------------------------------------------------------|------------|
| ![](Demonstration/Demonstration.GIF)        | Current state of the webapp. |

##TODO
- Upload Working example
- Upload Demonstartion video & GIF
- Share with collaborator

## Contributions

Pull requests are appreciated! 
