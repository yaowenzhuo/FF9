# -*- coding: utf-8 -*-
"""Build complete FFIX magazine by reading parts and assembling."""
import os, glob

base = r"C:\Users\Stella\Desktop\ffix-magazine\parts"
output = r"C:\Users\Stella\Desktop\ffix-magazine\index.html"

parts = sorted(glob.glob(os.path.join(base, "*.html")))
if not parts:
    print("No parts found!")
    exit(1)

with open(output, 'w', encoding='utf-8') as out:
    for p in parts:
        with open(p, 'r', encoding='utf-8') as f:
            out.write(f.read())
        out.write('\n')

size = os.path.getsize(output)
print(f"Assembled {len(parts)} parts into {output}")
print(f"File size: {size:,} bytes ({size/1024:.1f} KB)")
