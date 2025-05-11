import string
s = open("24.txt").read()
t = "GHIJKLMNOPQRSTUVWXYZ"
for x in t:
    s = s.replace(f"{x}", " ")
s = s.split()
r = []
for i in s:
    if i.count("B") == 10:
        r.append([int(i,16),i])

h = max(r)[1]
print(len(h))
print(len(str(max(r)[0])))