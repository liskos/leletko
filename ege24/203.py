s = open("24data/24-203.txt").read()
k = 0
for i in range(len(s)):
    l = i
    for r in range(l, len(s)):
        otr = s[l:r+1]
        if "A" in otr and "B" in otr and "C" in otr:
            break
        if r-l + 1 >= 3:
            k += 1
print(k)
