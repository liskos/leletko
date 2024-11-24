def f(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+1, b) + f(a+3, b) + f(a*2, b)

print(f(1, 4) * f(4, 9) * f(9, 13))