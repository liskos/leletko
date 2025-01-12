def f(a,b):
    if a == b:
        return 1
    if a < b or a == 40:
        return 0
    return f(a-3, b) + f(a//2,b) + f(a//5,b)

print(f(120,49) * f(49,6))