#!/usr/bin/env python3
"""Entry for make.fun bounty news-image-20261127.

Copies the repo's entry.png (a 1024x1024 PNG summing up the world news
of Friday 27 November 2026) to /output/entry.png. Standard library only.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.png")

if not os.path.isfile(SRC):
    sys.exit("entry.png missing next to main.py")
os.makedirs(os.path.dirname(DST), exist_ok=True)
shutil.copyfile(SRC, DST)
digest = hashlib.sha256(open(DST, "rb").read()).hexdigest()
print("wrote", DST, os.path.getsize(DST), "bytes, sha256", digest)
