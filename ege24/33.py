s = open("24data/k7c-1.txt").read()
s = s.replace("A", " ")
s = s.split()
r = []
for x in s:
    if len(x) == 3 and x[0] in "BCD" and (x[1] in "BDE" and x[1] != x[0]) and (x[2] in "BCE" and x[2] != x[1]):
        r.append(x)
print(len(r))