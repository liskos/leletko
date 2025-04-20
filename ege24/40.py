d = open("24data/k7-m2.txt").read()
s = d.replace("A", " ").replace("B", " ")
s = s.split()
r = []
for x in s:
    r.append(len(x))

print(max(r), len(r), len(d))