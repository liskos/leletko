s = open("24data/k8-4.txt").read()
i = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
r = []
h = 0
for x in i:
    t = str(x)
    while t in s:
        t += str(x)
    r.append(len(t))
    if len(t) == 5:
        h = t[0]
        break

print(h,max(r))