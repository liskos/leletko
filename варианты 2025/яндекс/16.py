import sys
sys.setrecursionlimit(100000)
def f(n):
    if n == 42:
        return 42
    if n > 42:
        return (n + 1) * (n - 1) * f(n - 1)

print((f(2042) + f(2043)) / f(2041))