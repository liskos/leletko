d = open("24data/k7-m6.txt").read()
f = d
d = d[::-1]
s = d.replace("A", " ").replace("B", " ")
s = s.split()
k = 0
for x in s:
    k += 1
    g = len(x)
    d = d.replace(f"{x}", f"{k}",1)

print(k)
print(f[:35])
print(d[:35])