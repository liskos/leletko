def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b += "00"
    else:
        b += "11"
    return int(b, 2)

for i in range(1, 100000):
    if f(i)>150:
        print(f(i))
        break