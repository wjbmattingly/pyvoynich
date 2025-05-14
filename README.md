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
from pyvoynich.data import STA_Eva_Bint, Eva_Cuva

# Create a Bitrans instance with default rules
bitrans = Bitrans()
    
# Test a simple translation
input_text = "P2A3K1A2C2.A2Q1A3B2.A3C1.A3Q2A3G1.L1A1B2.L1A1C1A2.U2C1J1C2.A2.Q1A1C1.L1A1B2B1A2"
output_text = bitrans.translate(input_text)
print(f"Input: {input_text}")
print(f"Output with default rules: {output_text}")

# Test with different rule sets
bitrans_bint = Bitrans(STA_Eva_Bint)
output_bint = bitrans_bint.translate(input_text)
print(f"Output with STA_Eva_Bint rules: {output_bint}")

bitrans_cuva = Bitrans(Eva_Cuva)
output_cuva = bitrans_cuva.translate(input_text)
print(f"Output with Eva_Cuva rules: {output_cuva}")
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