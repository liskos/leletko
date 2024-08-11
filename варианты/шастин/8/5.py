def f(n):
    b = sorted(str(n))
    c = (int(b[0]) + int(b[4])) ** 2
    d = 1
    for i in range(0,5):
        if int(b[i]) % 2 == 0:
            d = d * int(b[i])
    a = ""
    if d > c:
        a = str(d) + str(c)
    else:
        a = str(c) + str(d)
    return a


print(f(82134))
for b in range(10000, 100000):
    if f(b) == 12116:
        print(b)