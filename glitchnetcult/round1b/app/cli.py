#!/usr/bin/env python3
"""
Entrypoint for persona/section analysis.
"""
import argparse, json, pathlib
from round1b.app.pipeline import analyse
from round1b.app.utils import setup_logging

def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--persona", required=True)
    ap.add_argument("--job", required=True)
    ap.add_argument("--docs", default="/app/input")
    ap.add_argument("--out", default="/app/output/output.json")
    ap.add_argument("--use_keywords", action="store_true")
    return ap.parse_args()

def main():
    setup_logging("persona-analyst")
    a = parse_args()
    res = analyse(a.docs, a.persona, a.job, use_keywords=a.use_keywords)
    pathlib.Path(a.out).write_text(json.dumps(res, indent=2))
    print(f"Analysis written to {a.out}")

if __name__ == "__main__":
    main()
