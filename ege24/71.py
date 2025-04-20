s = open("24data/k8-100.txt").read()
i = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
r = []
g = []
h = 0
for x in i:
    t = str(x)
    while t in s:
        t += str(x)
    r.append(len(t)-1)
    if len(t) == 4501:
        g.append(t[:-1])

print(max(r))

for i in range(len(s)-max(r)-1):
    if s[i:i+max(r)] in g:
        print(s[i:i+max(r)][0],max(r))
        break