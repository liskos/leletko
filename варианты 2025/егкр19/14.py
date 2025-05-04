def f(n):
    b = ""
    while n > 0:
        b = b + str(n%4)
        n = n // 4
    return b.count("0")

m = 0
z = 0
for x in range(1,3001):
    a = 4**210 + 4**110 - x
    if f(a) > m:
        m = f(a)
        z = x
print(z)