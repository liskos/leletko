def f(n):
    if n > 16:
        return n - 3
    if n <= 16:
        return 2 * f(n + 1) + 2 * n + 3


print(f(2))