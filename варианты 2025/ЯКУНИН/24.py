import sys
sys.stdin=open("24.txt")
s = input()
t = s[0]
m = 0
for i in s[1:]:
    if (t[-1] in "AEIOYU") == (i in "AEIOYU"):
        t += i
    else:
        t = i
    m = max(m, len(t))
print(m)
