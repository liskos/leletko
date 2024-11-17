def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n//3) + 3

print(f(999))