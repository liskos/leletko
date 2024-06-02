def f(n):
    b = bin(n)[2:]
    a = b.count("1")
    b = b + str(a % 2)
    a = b.count('1')
    b = b + str(a % 2)
    return int(b, 2)

for i in range(1, 1000):
    if f(i) < 70:
        print(f(i))
