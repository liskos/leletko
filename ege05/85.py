def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b += "11"
    else:
        b += "00"
    return int(b, 2)

for i in range(1, 100000):
    if f(i)>54:
        print(f(i))
        break