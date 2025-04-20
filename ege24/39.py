d = open("24data/k7-m1.txt").read()
s = d.replace("A", " ").replace("B", " ")
s = s.split()
r = []
for x in s:
    r.append(len(x))

print(min(r), len(r), len(d))