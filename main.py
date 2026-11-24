"""One Word, First Thought (program/v1): write the competition entry word unchanged: 'gloaming'."""
import os
from pathlib import Path


def main() -> None:
    # MAKEFUN_OUTPUT_DIR lets tests redirect the output without touching /output.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text("gloaming", encoding="utf-8")


if __name__ == "__main__":
    main()
