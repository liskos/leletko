def f(n):
    b = bin(n)[2:]
    b = b.zfill(8)
    d = b[:2] + b[-2:]
    return int(d, 2)

for i in range(1, 110):
    if f(i) == 7:
        print(i)