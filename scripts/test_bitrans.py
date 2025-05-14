# #!/usr/bin/env python3
# """
# Test script for the Bitrans class.
# """

# import sys
# import os
# import tempfile

# # Add the parent directory to the path so we can import the pyvoynich package
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pyvoynich.bitrans import Bitrans
from pyvoynich.data import STA_Eva_def, STA_Eva_Bint, Eva_Cuva

def test_basic_translation():
    """Test basic translation functionality."""
    # Create a Bitrans instance with default rules (STA_Eva_def)
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



if __name__ == "__main__":
    test_basic_translation()