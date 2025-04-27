s = open("24data/k8-0.txt").read()
m = 0
t = s[0]
r = []
t_best = []
for i in s[1:]:
    if t[-1] == i:
        t += i
        if len(t) >= m:
            m = len(t)
            t_best.append(t)
    else:
        t = i
for st in t_best:
    if len(st) == m:
        print(st[0], m)