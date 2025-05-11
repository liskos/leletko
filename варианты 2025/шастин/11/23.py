def f(a,b):
    if a == b:
        return 1
    if a < b or a == 20:
        return 0
    return f(a-2,b) + f(a-3,b) + f(a**0.5//1,b)


print(f(26,3))
