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