def f(a, b):
    if a == 10:
        return 0
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+1, b) + f(a+5, b)

print(f(2, 15) * f(15, 26))