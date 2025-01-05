s = open("24.txt").readline()
t = ""
m = 0
ts = ""
for i in s:
    t += i
    while len(t) != len(set(t)):
        t = t[1:]
    if len(t) > m:
        m = len(t)
        ts = t
print(m, ts)