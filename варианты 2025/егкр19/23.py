def f(a,b):
    if a == b:
        return 1
    if a > b or a == 56:
        return 0
    return f(a+3,b) + f(a+7,b) + f(a*3,b)

print(f(12,40)*f(40,72)*f(72,89))