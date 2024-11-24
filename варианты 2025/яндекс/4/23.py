def f(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+2, b) + f(a**2, b) + f(a+5, b)

print(f(4, 34) + f(4, 31))