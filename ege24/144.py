s = open("24data/24-j6.txt").read()
t = s[0]
r = []
k = 0
for i in range(1,len(s)-1):
    if t[-1] < s[i]:
        t += s[i]
    else:
        r.append(t)
        t = s[i]

for i in r:
    if len(i) == 5:
        k += 1

print(k)