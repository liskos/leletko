def f(n):
    if n < 3:
        return n + 3
    if n >= 3 and n % 3 == 0:
        return (n + 2) * f(n - 4)
    if n >= 3 and n % 3 != 0:
        return n + f(n - 1) + f(n - 2)


print(f(20))