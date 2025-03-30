import sys
sys.setrecursionlimit(1000000)

def f(a,b):
    if a == b:
        return 1
    if a < b:
        return 0
    if a % 3 == 0:
        return f(a-5,b) + f(a//3,b)

    return f(a-5,b) + f(a - a%3,b)


print(f(103,73) * f(73,24))