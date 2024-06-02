def f(n):
    b = bin(n)[2:]
    b = b.zfill(8)
    d  =  str(b[0]) + str(b[1]) + str(b[2]) + str(b[3] + str(b[4]) + str(b[5]))
    return int(d, 2)

a = set()
for i in range(20, 600):
    a.add(f(i))
print(len(a))
