import sys
sys.stdin=open("24.txt")
s = input()
t = s[0]
su = 0
r = []
m = 0
for i in range(1, len(s)):
    if t[0] in "+*" or (t[-1] in "+*" and s[i] in "+*"):
        t = s[i]
        su = 0
    elif t[-1] == "+" and s[i] in "789":
        t += s[i]
        su += int(s[i])
    elif t[-1] in "789" and s[i] in "+":
        t += s[i]
    elif t[-1] in "789" and s[i] in "789":
        dp = 0
        while i <= len(s) and t[-1] in "789" and s[i] in "789":
            t += s[i]
            dp += int(s[i])
            i = i + 1
        su += dp
        if su > m:
            m = su

print(m)