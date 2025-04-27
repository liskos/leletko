s = open("24data/24-2.txt").read()
r = ""
m = 0
t = s[0]
for i in s[1:]:
    if t and t[-1] < i:
        t += i
        if len(t) > m:
            m = len(t)
            r = t
    else:
        t = i
print(r)