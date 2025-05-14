import os
from pathlib import Path
import requests

# List of files to download
files = [
    "Curr-Eva_def.bit",
    "Eva-Cuva.bit",
    "EvaT.bit",
    "FSG-Eva_def.bit",
    "STA-Curr_def.bit",
    "STA-EvaT_def.bit",
    "STA-Eva_Bint.bit",
    "STA-Eva_Eint.bit",
    "STA-Eva_def.bit",
    "STA-FSG_def.bit",
    "STA-v101_def.bit",
    "STA_L0-1.bit",
    "STA_L0-2.bit",
    "bitrans.c",
]

base_url = "https://www.voynich.nu/software/bitrans/"
out_dir = Path(__file__).parent.parent / "original"
out_dir.mkdir(parents=True, exist_ok=True)

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}  # Accept any content type and mimic a browser

for fname in files:
    url = base_url + fname
    out_path = out_dir / fname
    print(f"Downloading {fname} as raw text...")
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    # Save as text regardless of content type
    with open(out_path, "w", encoding="utf-8", errors="replace") as f:
        f.write(r.text)
    print(f"Saved to {out_path}")
