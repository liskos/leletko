def f(a, b):
    if a == 8 or a == 11:
        return 0
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+1, b) + f(a+2, b) + f(a*3, b)

print(f(2, 5) * f(5, 21))