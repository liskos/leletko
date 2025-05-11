s = open("24data/24-197.txt").read()
# s = s.replace("ZXY", "A").replace("ZYX", "A")
# s = s.replace("Z", " ").replace("X", " ").replace("Y", " ")
# s = s.split()
# print(len(max(s, key=len)))

import re

pat = r"((ZXY)|(ZYX))+"
r = max([len(x.group()) for x in re.finditer(pat,s)])
print(r//3)