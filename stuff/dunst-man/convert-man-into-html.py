#!/usr/bin/env python3
'''
convert_dunst_man_to_html_indent.py

Converts dunst-man.txt to HTML using indentation levels:
- 0 spaces: <h1>
- 3 spaces: <h2>
- 7 spaces: <h3>
- 11 spaces: <p>
- 15 spaces: <h4>
Lines not matching these exact indents are ignored.
'''
from pathlib import Path
from html import escape

INPUT = 'dunst-man.txt'
OUTPUT = 'index.html'

lines = Path(INPUT).read_text(encoding='utf-8').replace('\r', '').splitlines()
out = []

# HTML header
out.append('<!DOCTYPE html>')
out.append("<html lang='en'>")
out.append('<head>')
out.append("  <meta charset='UTF-8'>")
out.append('  <title>Dunst Man Page</title>')
out.append("<link rel='stylesheet' href='style.css'>")
out.append("<link href='https://fonts.googleapis.com/css2?family=Cascadia+Code&display=swap' rel='stylesheet'>")
out.append('</head>')
out.append("<body><p style='color:rgb(159, 159, 159); position:sticky; top:0; background: rgba(35, 35, 35, 0.46);'>Anything that is red means that I didn't assign the number of spaces to a heading tag.</p>")

for line in lines:
    stripped = line.rstrip('\n')
    spaces = len(stripped) - len(stripped.lstrip(' '))
    content = stripped.strip()
    if not content:
        continue  # skip empty lines

    if spaces == 0:
        out.append(f'<h1>{escape(content)}</h1>')
    elif spaces == 3:
        out.append(f'<h2>{escape(content)}</h2>')
    elif spaces == 7:
        out.append(f'<h3><i>{escape(content)}</i></h3>')
    elif spaces == 11:
        out.append(f'<p>{escape(content)}</p>')
    elif spaces == 15:
        out.append(f'<h4><i>{escape(content)}</i></h4>')
    else:
        # highlight other lines
        out.append(f"<h3 style='color:#ff6161'><i>{escape(content)}</i></h3>")
        continue

out.append('</body>')
out.append('</html>')

Path(OUTPUT).write_text('\n'.join(out), encoding='utf-8')
print(f'Generated {OUTPUT}')
