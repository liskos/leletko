def f(a,b):
    if a == b:
        return 1
    if a < b:
        return 0
    if a > b:
        if a % 2 == 0 and a % 3 == 0:
            return f(a//2,b) + f(a//3,b) + f(a-1,b)
        if a % 2 != 0 and a % 3 == 0:
            return f(a-1,b) + f(a//3,b)
        if a % 2 == 0 and a % 3 != 0:
            return f(a-1,b) + f(a//2,b)
        if a % 2 !=0 and a % 3 != 0:
            return f(a-1,b)

print(f(122,57) * f(57,11))