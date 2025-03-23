s = open("24(2).txt").read()
m = 10**10
t = ""
k = 0
for i in range(len(s)):
    t += s[i]
    if len(t) >= 5:
        if t[-5:-2] == t[-3:]:
            k += 1
    while k > 170:
        if t[:3] == t[2:5]:
            k -= 1
        t = t[1:]
    if k == 170:
        m = min(m, len(t))
    if i % (len(s) // 100) == 0:
        print(i // (len(s) // 100) , "%")
print(m)