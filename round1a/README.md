
# Round1A: PDF Outline Extractor

Extracts section outlines from PDF files and outputs them as JSON.

## Usage

### Docker
```
docker build --platform linux/amd64 -t outline-extractor .
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none outline-extractor
```

### Local
```
python -m round1a.app.cli
```

- Place PDFs in the `input/` folder.
- JSON results will be in the `output/` folder.
