def f(a,b):
    if a == 60:
        return 0
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a+1, b) + f(a*2, b) + f(a*3, b)

print(f(10, 30) * f(30, 70))