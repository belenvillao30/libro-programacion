"""
modo_github.py — Convierte CSS inline → <link> externo para GitHub Pages
Ejecutar desde la carpeta del libro:  python3 modo_github.py
"""
import re, os

LINK = '<link rel="stylesheet" href="estilos.css">'
ok = 0
for fname in sorted(os.listdir('.')):
    if not fname.endswith('.html'): continue
    with open(fname) as f: c = f.read()
    nuevo = re.sub(r'<style>.*?</style>', LINK, c, count=1, flags=re.DOTALL)
    if nuevo != c:
        with open(fname, 'w') as f: f.write(nuevo)
        ok += 1
print(f'✅ {ok} archivos → usan estilos.css externo (modo GitHub Pages)')
