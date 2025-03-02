s = open("24(1).txt").read()
import re

a = max(map(int, re.findall(r"[1-9][0-9]+[02468]", s)))
print(a)