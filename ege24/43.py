d = open("24data/k7-m5.txt").read()
f = d
d = d[::-1]
s = d.replace("A", " ").replace("B", " ")
s = s.split()
k = 0
for x in s:
    k += 1
    g = len(x)
    d = d.replace(f"{x}", f"{g}",1)

print(k)
print(f[:15], f[-15:])
print(d[:15], d[-15:])