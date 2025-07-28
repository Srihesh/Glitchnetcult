# Glitchnetcult PDF Analysis Toolkit

A toolkit for extracting outlines and analyzing PDF content. Supports Docker and local runs. Place PDFs in `input/`, get JSON results in `output/`. Includes persona/job-based section ranking and summarization. MIT License.

## Usage

### Build Docker Image (Round1A)
```
docker build --platform linux/amd64 -t outline-extractor round1a
```

### Run with Docker (Round1A)
```
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none outline-extractor
```

### Run Locally (Round1A)
```
python -m round1a.app.cli
```

### Run Locally (Round1B)
```
python -m round1b.app.cli --persona "Document Manager" --job "Summarize document features" --docs "input" --out "output/output.json"
```
