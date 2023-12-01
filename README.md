<p align="center"><img src="https://github.com/E2-RJ/Assets_ecosystem2/blob/main/Full_Logo/e2_full_logo_navy.svg" /></p>

API microservice, using Python and FastAPI, for testing files against industry schemas. Data validation uses Pandera.

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

Fast API endpoints are hosted in main.py in the root directory
- /schemamodels/models contain the Pandera schema model files
- /schemamodels/models/controlled_lists contains the controlled list as a .csv to be updated
- updated or new controlled lists are imported into the relevant Pandera schema

## Production Instructions

A docker file and github workflow is included within this repository. When a release is created, the docker container is built and submitted to dockerhub.

It is assumed you already have accounts for [Dockerhub](https://hub.docker.com) and [Github](https://github.com), along with a [Docker](https://www.docker.com/get-started/) instance set up for the built container to run on. If any information is needed on how ecosystem2 handles hosting, please reach to us via our [website](https://ecosystem2.co.uk) or [email](mailto:hello@ecosystem2.co.uk).

### Seting up dockerhub access token
- Once logged into Dockerhub, select the downward triangle next to your username on the far right of your screen.
  <p align="left"><img src="https://github.com/E2-RJ/Assets_ecosystem2/blob/main/Screenshot_Dockerhub-NavBar.png?raw=true" /></p>
- A dropdown should present itself, use this to **enter your account settings**
  <p align="left"><img src="https://github.com/E2-RJ/Assets_ecosystem2/blob/main/Screenshot_Dockerhub-Dropdown.png?raw=true" /></p>
- On the sidebar to the left, **Select Security**
  <p align="left"><img src="https://github.com/E2-RJ/Assets_ecosystem2/blob/main/Screenshot_Dockerhub-Security.png?raw=true" /></p>
- To the right of the Access Tokens heading, **Click on the blue New Access Token button**
  <p align="left"><img src="https://github.com/E2-RJ/Assets_ecosystem2/blob/main/Screenshot_Dockerhub-AddToken.png?raw=true" /></p>
- A popup should now appear in the centre of the screen, **Set the appropriate description and permissions**
  <p align="left"><img src="https://github.com/E2-RJ/Assets_ecosystem2/blob/main/Screenshot_Dockerhub-NewToken.png?raw=true" /></p>
- Your new token should now be created, **Copy the token**
  <p align="left"><img src="https://github.com/E2-RJ/Assets_ecosystem2/blob/main/Screenshot_Dockerhub-Token.png?raw=true" /></p>

### Setting up dockerhub credentials
- Below the repository name, in the top left corner of the screen, there is a navigation bar; **Select Settings**
  <p align="left"><img src="https://github.com/E2-RJ/Assets_ecosystem2/blob/main/Screenshot_Repo-Bar.png?raw=true" /></p>
- You should be presented with a page consisting with a sidbar and the repositories settings, **Select Secrets and variables**
  <p align="left"><img src="https://github.com/E2-RJ/Assets_ecosystem2/blob/main/Screenshot_RepoSettings-Sidebar.png?raw=true" /></p>
- With the sub-section expanded, **Select Actions**
  <p align="left"><img src="https://github.com/E2-RJ/Assets_ecosystem2/blob/main/Screenshot_Repo-Secrets.png?raw=true" /></p>
- This section **should already have two repository secrets, DOCKER_USERNAME and DOCKER_PASSWORD**
  <p align="left"><img src="https://github.com/E2-RJ/Assets_ecosystem2/blob/main/Screenshot_Docker_Credentials.png?raw=true" /></p>
- **If this is not the case, please add them**
- Assuming both secrets are present, **Select the pencil icon to edit each secret**

### Building docker container
- On the left sidebar, **Select Releases**
- **Select Draft New Release**
- Type in a new [version number](https://semver.org/) into tag field and select "Create new tag on publish".
- Set the target branch to main
- Either type the title and descript manually or select "Generate release notes"
- Press the green button that says "Publish release"
- Wait for the build to complete

| Screenshot                                                            | Description|
|-----------------------------------------------------------------------|------------|
| ![](Demonstration/Demonstration.GIF)        | Current state of the webapp. |

###TODO
- Upload Working example
- Upload Demonstartion video & GIF
- Share with collaborator

## Contributions

Pull requests are appreciated! 
