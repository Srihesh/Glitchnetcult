### Build
docker build --platform linux/amd64 -t outline-extractor round1a

### Run (hackathon harness does this automatically)
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output \
           --network none outline-extractor
