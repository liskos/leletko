def f(n):
    s = bin(n)[2:]
    s = s[::-1]
    return int(s, 2)

for n in range(1000, 10000):
    if f(n) == 29:
        print(n)
