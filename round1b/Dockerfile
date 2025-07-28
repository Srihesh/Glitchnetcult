FROM --platform=linux/amd64 python:3.11-slim

WORKDIR /app

# Install dependencies
COPY round1b/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt \
 && useradd -ms /bin/bash runner

USER runner

# Bring in code (stage 1 and 2 code; robust for import)
COPY round1a/app/ /app/app_round1a/
COPY round1b/app/ /app/app/
COPY round1b/tests/ /app/tests/        
COPY configs/ /app/configs/             

# Entrypoint
ENTRYPOINT ["python", "-m", "app.cli"]
