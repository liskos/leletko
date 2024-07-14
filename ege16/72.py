
import sys
sys.setrecursionlimit(1000000)
def f(n):
    if n <= 70:
        return f(n + 2) + 2 * f(3 * n)
    if n > 70:
        return n - 50

print(f(40))