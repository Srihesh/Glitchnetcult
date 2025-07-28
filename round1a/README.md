# Round1B: Persona-Based PDF Analysis

Analyzes PDF content for a given persona and job, ranking and summarizing relevant sections.

## Usage

```
python -m round1b.app.cli --persona "Document Manager" --job "Summarize document features" --docs "input" --out "output/output.json"
```

- Place PDFs in the `input/` folder.
- Results are written to `output/output.json`.
