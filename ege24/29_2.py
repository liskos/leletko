import re

s = open("24data/k7b-3.txt").read()
pattern = (r"(BAFE)+(BAF|BA|B)?")
r = [ len(x.group()) for x in re.finditer(pattern,s)]
print(max(r))