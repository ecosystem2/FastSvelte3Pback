FROM python:3-slim-buster

# Create app directory
RUN mkdir /src
WORKDIR /src

# Install app dependencies
COPY requirements.txt .

RUN pip uninstall wheel
RUN pip install -r requirements.txt

# Bundle app source
COPY . .

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=5173"]