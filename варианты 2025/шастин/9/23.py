def f(a,b):
    if a == b:
        return 1
    if a < b or a == 26 or a == 30:
        return 0
    return f(a-3,b) + f(a//2+1,b)

print(f(69,14))