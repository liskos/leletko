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
x = 0
for i in range(1, 1000000):
    if f(i) < 10 ** 6:
        x = i
print(x)