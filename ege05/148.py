def f(n):
    b = bin(n)[2:]
    a = int(b)
    c = str(a) + str(a % 2)
    if b.count("1") % 2 == 0:
        c += "0"
    else:
        c += "1"
    if c.count("1") % 2 == 0:
        c += "0"
    else:
        c += "1"
    return int(c, 2)


for i in range(1, 100):
    if f(i) > 90:
        print(i)