def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b = "10" + b[2:] + "0"
    else:
        b = "1" + b[:-2] + "10"
    return int(b, 2)

print(f(6))
print(f(4))
for i in range(1, 1000):
    if f(i) < 224:
        print(i)