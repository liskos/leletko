import sys
sys.setrecursionlimit(10000)
def f(n):
    if n < 10:
        return g(n) == n
    if n > 9:
        return 3 * n + g(n - 2)

def g(n):
    if n > 9:
        return n - 2 + f(n - 1)

print(f(2204) - g(2200))