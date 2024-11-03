def f(a,b):
    if a == 12:
        return 0
    if a == b:
        return 1
    if a < b:
        return 0
    return f(a - 2, b) + f(a // 2, b)

print(f(42,26) * f(26, 1))