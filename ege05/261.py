def f(n):
    b = bin(n)[2:]
    if b.rfind("0") != -1:
        b = b[:b.rfind("0")] + b[:2] + b[b.rfind("0") + 1 :]
    b = b[::-1]
    return int(b, 2)


a = set()
for i in range(1, 1000):
    if f(i) == 127:
        a.add(i)
print(len(a))
print(a)