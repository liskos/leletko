import sys
sys.setrecursionlimit(10000)
def f(n):
    if n > 10000:
        return n + 6
    if n <= 10000:
        return 2 * n + 8 + f(n + 4)

print(f(1092) - f(1104))