def f(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    x, y = 0, 0
    if b % 2 == 0:
        x = f(a, b//2)
    if b % 3 == 0:
        y = f(a, b//3)
    return f(a, b-1) + x + y

print(f(2, 15) * f(15,30))