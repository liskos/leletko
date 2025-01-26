def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a+2,b) + f(a+3,b) + f(a*2,b)

print(f(8,20) * f(20,30) * f(30,35))