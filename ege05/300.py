def f(n):
    b = bin(n)[3:]
    if b.count("1") % 2 == 0:
        b = "10" + b
    else:
        b = "1" + b + "0"
    return int(b, 2)


for i in range(1, 1000):
    if f(i) < 450:
        print(f(i))
print(f(4))