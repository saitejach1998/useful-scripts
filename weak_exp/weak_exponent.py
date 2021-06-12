import sys
from gmpy2 import mpz,iroot

e = 3
ct= mpz("80505397907128518326368510654343095894448384569115420624567650731853204381479599216226376345254941090872832963619259274943986478887206647256170253591735005504")


pt_num = iroot(ct,e)[0]
print(f"PT decimal rep: {pt_num}")


pt_hex = hex(int(pt_num))
print(f"PT hex rep: {pt_hex}")


bytes_object = bytes.fromhex(pt_hex[2:])
ascii_text = bytes_object.decode("ASCII")
print(f"Ascii Rep : {ascii_text}")
