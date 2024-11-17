def f(a, b):
    if a == 8:
        return 0
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+1, b) + f(a*2, b)

print(f(2, 20)*  f(20, 40))