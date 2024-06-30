def f(n):
    b = bin(n)[2:]
    if b.count("1") % 4 == 0:
        b = "10" + b
    else:
        b = "11" + b
    if int(b, 2) % 2 == 0:
        b = b + "1"
    else:
        b = b + "0"
    return int(b, 2)


print(f(13))
print(f(10))
for i in range(1, 1000):
    if f(i) <= 250:
        print(i)