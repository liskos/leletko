def f(a, b):
    if a == 35:
        return 0
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+1, b) + f(a*3, b) + f(a*4,b)

print(f(2, 8)*  f(8, 70))