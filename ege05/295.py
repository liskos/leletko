def f(n, m):
    b = bin(n)[2:]
    sn = b.count("1") ** 2
    sm = bin(m)[2:].count("1") ** 2
    return sn - sm


a =[]
for n in range(1, 10000):
    for m in range(1, 10000):
        if f(n, m) == 33:
            a.append(n + m)
print(min(a))

