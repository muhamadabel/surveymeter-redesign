#!/usr/bin/env python3
"""Check every internal href/src in the built site points at a file that exists."""
import os
import re
import sys
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = {'legacy', 'templates', 'tools', 'content', '.git', 'node_modules'}

broken, pages = {}, 0
for dirpath, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in SKIP]
    for f in files:
        if not f.endswith('.html'):
            continue
        pages += 1
        src = open(os.path.join(dirpath, f), encoding='utf-8').read()
        for ref in re.findall(r'(?:href|src)="(/[^"#]*)', src):
            path = urllib.parse.unquote(ref.split('?')[0])
            target = os.path.join(ROOT, path.lstrip('/'))
            ok = os.path.isfile(target) or os.path.isfile(os.path.join(target, 'index.html'))
            if not ok:
                broken.setdefault(path, set()).add(os.path.relpath(os.path.join(dirpath, f), ROOT))
print(f'{pages} pages checked, {len(broken)} broken internal targets')
for path, where in sorted(broken.items())[:40]:
    print(' ', path, '<-', sorted(where)[:2], f'(+{len(where) - 2})' if len(where) > 2 else '')
sys.exit(1 if broken else 0)
