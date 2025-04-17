import re

s = open("24data/k7-44.txt").read()
pattern = r"[C]+"
r = [len(x.group()) for x in re.finditer(pattern,s)]
print(max(r))