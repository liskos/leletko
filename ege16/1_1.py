import sys
sys.setrecursionlimit(10000)
def f(n):
    if n == 1:
        return 1
    return 2 * f(n - 1) + n + 3


print(f(1000))