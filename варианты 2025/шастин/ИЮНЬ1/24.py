s = open("24.txt").read()
k = l = m = 0
for r in range(2,len(s)):
    if s[r-2:r+1] == "LND":
        k += 1
    while k > 10000:
        if s[l:l+3] == "LND":
            k -= 1
        l += 1
    for l1 in range(l,r):
        if s[l1] == s[r]:
            m = max(m,r-l1+1)
            break

print(m)