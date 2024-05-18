def f(n):
    b = bin(n)[2:]
    b = int(b)
    b = str(b) + str(b % 2)
    if b.count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    if b.count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    return int(b, 2)


for i in range(1, 100):
    if f(i) > 114:
        print(i)