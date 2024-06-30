def f(n):
    b = bin(n)[2:]
    if n % 6 == 0:
        b = b + "111"
    else:
        b = b + "1"
    if int(b, 2) % 3 == 0:
        b = b + "101"
    else:
        b = b + "1"
    return int(b, 2)


print(f(12))
for i in range(1, 100000):
    if f(i) > 300000:
        print(i)
        break