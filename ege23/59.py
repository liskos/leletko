def f(a, b):
    if a == 12:
        return 0
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+1, b) + f(a*3, b)

print(f(4, 6)*  f(6, 50))