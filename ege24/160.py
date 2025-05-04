import string
d = open("24data/24-s1.txt").read()
m = 10000000
r = []
for s in open("24data/24-s1.txt"):
    if s.count("A") < m:
        r.append(s)
        m = s.count("A")

y = r[-1]
g = []
t = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in t:
    g.append([y.count(i),i])

print(min(g))
