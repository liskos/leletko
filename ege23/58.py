def f(a, b):
    if a == 10:
        return 0
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+1, b) + f(a*2, b)

print(f(1, 25)*  f(25, 28))