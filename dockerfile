FROM python:3.9

# Create app directory
WORKDIR /src

# Install app dependencies
COPY requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Bundle app source
COPY . /src/

EXPOSE 5173

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=5173", "--root-path", "/api"]