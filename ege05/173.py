def f(n):
    b = bin(n)[2:]
    b = b.zfill(8)
    d  =  str(b[0]) + str(b[1]) + str(b[2]) + str(b[3] + str(b[4]) + str(b[5]) + str(b[6]))
    d = d[::-1]
    return int(d, 2)

for i in range(1, 256):
    if f(i) == i:
        print(i)