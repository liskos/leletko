def f(n):
    if n > 15:
        return n
    if n <= 15:
        return 2 * f(n + 1) + 5 * n + 2


print(f(2))