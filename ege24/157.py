import string
s = open("24data/24-157.txt").read()
c = dict()
for i in range(len(s)-2):
    if s[i]==s[i+1]:
        keydict = s[i+2]
        c[keydict] = c.get(keydict, 0) + 1
m = max(c.values())
k = [x for x in c if c[x] == m]
print(min(k), m, sep="")
