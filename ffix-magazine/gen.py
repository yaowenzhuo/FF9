# -*- coding: utf-8 -*-
"""Generate the Final Fantasy IX digital magazine."""
import os, sys

OUT = r"C:\Users\Stella\Desktop\ffix-magazine\index.html"

# We'll build the file from a string
s = []

def w(x):
    s.append(x)

# Read existing parts
parts_dir = r"C:\Users\Stella\Desktop\ffix-magazine\parts"
if os.path.exists(parts_dir):
    for f in sorted(os.listdir(parts_dir)):
        fp = os.path.join(parts_dir, f)
        if os.path.isfile(fp):
            with open(fp, 'r', encoding='utf-8') as fh:
                w(fh.read())

# Write the assembled file
with open(OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(s))

sz = os.path.getsize(OUT)
print(f"Written {OUT}: {sz} bytes")
