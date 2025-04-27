import re
s = open("24data/24-1.txt").read()
pattern = r"([0-9])+"
r = [int(x.group()) for x in re.finditer(pattern, s) if all(i in "13579" for i in x.group())]
print(max(r))