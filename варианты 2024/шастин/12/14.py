from string import *

for x in (digits + ascii_uppercase)[:22]:
    s = int(f"56{x}c20", 22) + int(f"89{x}2", 22) + int(f"h24{x}k21", 22)
    if s % 21 == 0:
        print(s // 21)