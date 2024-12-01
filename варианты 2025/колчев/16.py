def f(n):
    if n <= 10:
        return n
    if n > 10 and n % 2 == 0:
        return 2 * f(n-2) + 6
    if n > 10 and n % 2 != 0:
        return f(n-1) + 2 * n

print(f(27) - f(20))