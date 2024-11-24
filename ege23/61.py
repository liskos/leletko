def f(a, b):
    if a == 6:
        return 0
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a+2,b) + f(a*3, b)

print(f(1, 25) * f(25, 63))