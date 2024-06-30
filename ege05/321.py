def f(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b + "11"
    else:
        b = b + "1"
    if int(b, 2) % 5 == 0:
        b = b + "101"
    else:
        b = b + "1"
    return int(b, 2)


print(f(7))
for i in range(1, 100000):
    if f(i) < 100000:
        print(i)