import string
s = open("24data/24-1.txt").read()
m = 0
t = s[0]
for i in s[1:]:
    if i in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" and int(t[-1],36) < int(i,36):
        t += i
        if len(t) > m:
            m = len(t)
    else:
        t = i
print(m)