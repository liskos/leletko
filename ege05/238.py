def f(n):
    n = str(n) + str(n % 10)
    n = int(n)
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    return int(b, 2)


for i in range(1, 1000):
    if f(i) > 413:
        print(i)
print(f(13))