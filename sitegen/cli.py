from __future__ import annotations

import argparse
from pathlib import Path
from .generator import build_site

def main() -> None:
    parser = argparse.ArgumentParser(description="Build Darshan's static portfolio.")
    parser.add_argument("command", choices=["build"], help="Command to run")
    parser.add_argument("--root", default=".", help="Project root directory")
    parser.add_argument("--output", default="dist", help="Output directory")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    output = (root / args.output).resolve()
    count = build_site(root, output)
    print(f"Built {count} pages into {output}")

if __name__ == "__main__":
    main()
