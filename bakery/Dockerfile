FROM python:3.10-slim

RUN pip install --upgrade pip --no-cache-dir

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .