s = open("24data/k8-80.txt").read()
import time
t1 = time.time()
m = 0
t = s[0]
t_best = ""
for i in s[1:]:
    if t[-1] == i:
        t += i
        if len(t) > m:
            m = len(t)
            t_best = t
    else:
        t = i
print(t_best[0], m)
print(time.time()-t1)
t2 = time.time()
import re
pattern = r"([A-Z0-9])(\1)+"
r = [x.group() for x in re.finditer(pattern, s)]
m = max(r, key=len)
print(m[0], len(m))
print(time.time()-t2)