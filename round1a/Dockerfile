# syntax=docker/dockerfile:1
FROM --platform=linux/amd64 python:3.11-slim

WORKDIR /app

COPY round1a/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt \
 && useradd -ms /bin/bash runner

USER runner

COPY round1a/app/ /app/app/

ENTRYPOINT ["python", "-m", "app.cli"]
