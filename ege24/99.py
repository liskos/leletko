s = open("24data/24-1.txt").read()
r = []
m = 0
t = s[0]
for i in s[1:]:
    if i != "\n" and int(t[-1],36) < int(i,36):
        t += i
        if len(t) > m:
            m = len(t)
            r.append(t)
    else:
        t = i
print(r[-1])