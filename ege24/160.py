import string
d = open("24data/24-s1.txt")
m = 10000000
t = ""
for s in d:
    mina = s.count("A")
    if mina < m:
        m = mina
        t = s
print(m, t)
g = []
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    g.append([t.count(i),i])
g.sort(key=lambda x: (x[0], x[1]), reverse=True)
bukva = g[0][1]
k = 0
d.close()
for s in open("24data/24-s1.txt"):
    k += s.count(bukva)
print(bukva, k)
