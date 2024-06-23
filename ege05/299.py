def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b = str(int(b[1:]))
    else:
        b = "1" + b + "00"
    if b.count("1") % 2 == 0:
        b = str(int(b[1:]))
    else:
        b = "1" + b + "00"
    return int(b, 2)


for i in range(1, 1001):
    if f(i) > 100:
        print(i)
        break

print(f(5))
