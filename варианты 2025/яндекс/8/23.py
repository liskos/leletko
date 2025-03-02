def f(a,b):
    if a == b:
        return 1
    if a > b or a == 20:
        return 0
    return f(a+3,b) + f(a*2,b) + f(a**2,b)


print(f(2,12) * f(12,128))
print(f(2,128))