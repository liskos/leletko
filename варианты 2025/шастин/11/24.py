import string
s = open("24.txt").read()
t = "GHIJKLMNOPQRSTUVWXYZ"
for x in t:
    s = s.replace(f"{x}", " ")
m = 0
for l in range(len(s)):
    k = 0
    for r in range(l, len(s)):
        if s[l] == "0": break
        if s[r] == " ": break
        if s[r] == "B": k += 1
        if k > 10: break
        if k == 10 and r - l +1 > m:
            m = r- l + 1
            print(m, s[l:r+1])
print(m)
