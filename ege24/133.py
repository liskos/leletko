import re
s = open("24data/24-j2.txt").read()
t = "FAIL"
g = []
for i in t:
    pattern = (fr"({i})*")
    r = max([len(x.group()) for x in re.finditer(pattern,s)])
    g.append(r)

print(max(g))