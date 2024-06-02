def f(n):
    b = bin(n)[2:]
    b = b.zfill(8)
    d  =  str(b[0]) + str(b[1]) + str(b[6]) + str(b[7])
    return int(d, 2)

for i in range(1, 256):
    if f(i) == 10:
        print(i)

