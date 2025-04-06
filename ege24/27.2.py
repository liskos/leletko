import re

s = open("24data/k7b-1.txt").read()
pattern = re.compile(r"(EAB)+(EA|E)")
rez = [x.group() for x in re.finditer(pattern,s)]
print(rez)
print(max(rez, key=len), len(max(rez, key=len)))