import sys
sys.setrecursionlimit(100000)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n + f(n - 1)

print(f(57693))