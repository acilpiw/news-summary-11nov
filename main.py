"""news-summary-01 entry (Python 3.13, standard library only).

Copies summary.txt beside this file to /output/entry.txt, byte for byte
(the summary is UTF-8 text of 1 to 2,000 characters, not only white space).
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
Deterministic: the same fixed summary is copied on every run; no network.
"""

import os
from pathlib import Path

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
summary = Path(__file__).resolve().parent / "summary.txt"
out_dir.mkdir(parents=True, exist_ok=True)
data = summary.read_bytes()
text = data.decode("utf-8")
assert 1 <= len(text) <= 2000 and text.strip(), "summary must be 1-2000 non-blank chars"
(out_dir / "entry.txt").write_bytes(data)
assert (out_dir / "entry.txt").read_bytes() == data
