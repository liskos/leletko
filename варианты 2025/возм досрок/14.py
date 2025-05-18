def pr(n):
    b = ""
    while n>0:
        b = b + str(n%5)
        n = n // 5
    return b[::-1]
zx = 0
m = 0
for x in range(1,2005+1):
    a = 5**150+5**98-x
    if pr(a).count("0") >= m:
        m = pr(a).count("0")
        zx = x

print(zx)
