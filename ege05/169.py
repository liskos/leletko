def f(n):
    s = bin(n)[2:]
    s = s[::-1]
    return int(s, 2)

for n in range(500, 1000):
    if f(n) == 19:
        print(n)