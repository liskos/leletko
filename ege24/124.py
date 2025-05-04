s = open("24data/24-1.txt").read()
r = []
counter = 0
for i in range(1, len(s) - 1):
    if s[i] < s[i - 1] and s[i] < s[i + 1]:
        counter += 1
        r.append(i)
    else:
        counter = 0

g = []
for i in range(len(r) - 1):
    g.append(r[i + 1] - r[i])
print(max(g))