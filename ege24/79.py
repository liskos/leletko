s = open("24data/k8-3.txt").read()
m = 0
t = s[0]
for i in s[1:]:
    if t[-1] != i:
        t += i
        if len(t) > m:
            m = len(t)
    else:
        t = i
print(m)