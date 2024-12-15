def f(a,b,k):
    if a == 40:
        return 0
    if a > b:
        return 0
    if a == b:
        return 1
    if k == 0:
        return f(a+1,b,0) + f(a*2, b,1) + f(a**2,b,0)
    if k == 1:
        return f(a+1,b,0) + f(a**2, b,0)

print(f(5,80,0) * f(80, 155,0))