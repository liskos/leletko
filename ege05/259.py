def f(n):
    b = bin(n)[2:]
    if b.rfind("0") != -1:
        b = b[:b.rfind("0")] + b[:2] + b[b.rfind("0") + 1 :]
    b = b[::-1]
    return int(b, 2)


for i in range(1, 1000):
    if f(i) == 119:
        print(i)
print(f(4))