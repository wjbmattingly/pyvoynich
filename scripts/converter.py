import os
import re
from pathlib import Path

SRC_DIR = Path(__file__).parent.parent / "original"
DST_FILE = Path(__file__).parent.parent / "pyvoynich" / "data.py"

# Helper to create a valid Python variable name from a file name
def make_var_name(filename):
    name = os.path.splitext(filename)[0]
    name = name.replace('-', '_').replace(' ', '_')
    if not name[0].isalpha():
        name = '_' + name
    return name

def parse_table_file(path):
    d = {}
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or line.startswith('<') or line.startswith('##BIT'):
                continue
            # Split on whitespace (first occurrence)
            parts = re.split(r'\s+', line, maxsplit=1)
            if len(parts) == 2:
                key, value = parts
                d[key] = value
    return d

def main():
    tables = {}
    for fname in os.listdir(SRC_DIR):
        if not fname.endswith('.bit'):
            continue
        varname = make_var_name(fname)
        table = parse_table_file(SRC_DIR / fname)
        tables[varname] = table
    # Write to data.py
    with open(DST_FILE, 'w', encoding='utf-8') as out:
        for varname, table in tables.items():
            out.write(f"{varname} = ")
            out.write(repr(table))
            out.write("\n\n")
    print(f"Wrote {len(tables)} tables to {DST_FILE}")

if __name__ == "__main__":
    main()
