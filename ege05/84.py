def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b += "1"
    else:
        b += "0"
    b += str(b.count("1") % 2)
    return int(b, 2)

for i in range(1, 100000):
    if f(i)>31:
        print(f(i))
        break