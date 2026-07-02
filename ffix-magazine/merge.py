import os, glob

parts_dir = r'C:\Users\Stella\Desktop\ffix-magazine\parts'
output = r'C:\Users\Stella\Desktop\ffix-magazine\index.html'

files = sorted(glob.glob(os.path.join(parts_dir, '*.html')))
print(f'Found {len(files)} part files')

content = ''
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        content += fh.read() + '\n'
    print(f'  + {os.path.basename(f)}')

with open(output, 'w', encoding='utf-8') as fh:
    fh.write(content)

size = os.path.getsize(output)
chars = len(content)
cjk = sum(1 for c in content if '\u4e00' <= c <= '\u9fff')
print(f'\nOutput: {output}')
print(f'File size: {size:,} bytes')
print(f'Total chars: {chars:,}')
print(f'CJK chars: {cjk:,}')
print('DONE')
