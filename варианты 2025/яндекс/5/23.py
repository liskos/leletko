import sys
sys.setrecursionlimit(10000)
def f(a,b):
    if a == 42 or a < b:
        return 0
    if a == b:
        return 1
    return f(a-1,b) + f(a//3,b) + f(a//4, b)

print(f(2025,250) * f(250,25))