s = open("24data/k8-31.txt").read()
i = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
r = []
h = 0
for x in i:
    t = str(x)
    while t in s:
        t += str(x)
    r.append(len(t)-1)
    if len(t) == 10:
        h = t[0]
        break

print(h,max(r))