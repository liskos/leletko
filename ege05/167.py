def f(n):
    s = bin(n)[2:]
    s = s[::-1]
    return int(s, 2)

for n in range(100, 1000):
    if f(n) == 9:
        print(n)
