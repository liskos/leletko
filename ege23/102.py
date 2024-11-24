def f(a, b):
    if a == 8:
        return 0
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+1, b) + f(a+4, b)  + f(a*4, b)

print(f(2, 6) * f(6, 24))