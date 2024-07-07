def f(n):
    if n <= 1:
        return 2
    if n > 1:
        return f(n - 1) + f(n - 2) + 4 * n
    

print(f(24))