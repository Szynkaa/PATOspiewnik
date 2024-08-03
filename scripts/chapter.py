#!/usr/bin/env python3

import locale
import sys
from pathlib import Path

if len(sys.argv) != 2:
    exit("No argument given")

locale.setlocale(locale.LC_COLLATE, "pl_PL.UTF-8")

directory = Path(sys.argv[1])
aggregate = directory.with_suffix(".tex")

if not directory.exists() or not directory.is_dir():
    exit("Directory does not exists")


with open(aggregate, "w", encoding="utf8") as output:
    for file in sorted(
        directory.glob("*.tex"),
        key=lambda file: locale.strxfrm(file.stem.replace("_", " "))
    ):
        print(f"\\newpage\\input{{{file}}}", file=output)

print(f"{aggregate} created")
