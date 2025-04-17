import re

s = open("24data/k7a-1.txt").read()
pattern = r"[ABC]+"
r = [len(x.group()) for x in re.finditer(pattern,s)]
print(max(r))