def f(a, b):
    if a == 15:
        return 0
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+1, b) + f(a+3, b)

print(f(2, 10) * f(10, 20))