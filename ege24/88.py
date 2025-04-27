import re
s = open("24data/24-1.txt").read()
pattern = r"([0-9])+"
r = [int(x.group()) for x in re.finditer(pattern, s) if int(x.group()) % 2 != 0]
print(min(r))