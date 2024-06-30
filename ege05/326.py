def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = "1" + b + str(b.count("1") % 2)
    else:
        b = b + "0" + str(b.count("1") % 2)
    return int(b, 2)


print(f(12))
print(f(5))
for i in range(1, 1000):
    if f(i) > 100:
        print(f(i), i)