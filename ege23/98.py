def f(a, b):
    if a == 25:
        return 0
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+1, b) + f(a*3, b) + f(a*2, b)

print(f(3, 12) * f(12, 46))