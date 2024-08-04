def f(n):
    if n < 2:
        return n
    if n >= 2:
        return n % 2 + 10 * f(n // 2)

for i in range(1, 10000000):
    if f(i) == 100000100001000100101:
        print(i)