def f(n):
    b = bin(n)[2:]
    b = b.zfill(8)
    d  =  b[:7]
    d = d[::-1]
    return int(d, 2)

for i in range(1, 100):
    if f(i) == i:
        print(i)