import sys
sys.stdin=open("24.txt")
s = input()
t = s[0]
r = []
for i in s[1:]:
    if t[0] in "*+0":
        t = i
    elif t[-1] in "*+" and i in "*+0":
        t = i
    else:
        t += i
    r.append(len(t))
print(max(r) - 1)