# PyVoynich

A Python package for bi-directional translation and substitution, particularly useful for working with Voynich manuscript transcriptions.

## Overview

PyVoynich is a Python implementation of the `bitrans.c` tool, which performs bi-directional translation/substitution based on a set of rules. The package is designed to be easy to use and integrate into Python applications. All the original C code and .bit files were written by René Zandbergen. For access to the original data and codebase, please visit [René Zandbergen's site](https://www.voynich.nu/software/000_README.txt).

Key features:
- Bi-directional translation (forward and reverse)
- Support for complex rule sets with multiple characters
- Loading rules from files
- Saving rules to files
- Processing text files

## Installation

```bash
# Clone the repository
git clone https://github.com/wjbmattingly/pyvoynich.git
cd pyvoynich

# Install the package
pip install -e .
```

## Usage

### Basic Usage

```python
from pyvoynich.bitrans import Bitrans
from pyvoynich.data import STA_Eva_def, STA_Eva_Bint, Eva_Cuva, Curr_Eva_def

input_text = "tchor. ckhoiin. daiin. cphchar-"

bitrans1 = Bitrans(STA_Eva_def, direction=2)
output1 = bitrans1.translate(input_text)
print(f"Output: {output1}")


input_text_sta = "Q2K1A1C1.U1A3G1.B1A3G1.T1K1A3C1"
bitrans2 = Bitrans(STA_Eva_def, direction=1)
output2 = bitrans2.translate(input_text_sta)
print(f"Output: {output2}")
```

## Available Rule Sets

The package includes several predefined rule sets:

- `STA_Eva_def`: Standard EVA transliteration
- `STA_Eva_Bint`: EVA to Beinecke transliteration
- `Eva_Cuva`: EVA to Currier transliteration
- `STA_FSG_def`: FSG transliteration
- `STA_Curr_def`: Currier transliteration

## Acknowledgements

This package is a Python implementation of the `bitrans.c` tool, originally developed for transliteration of the Voynich manuscript. 