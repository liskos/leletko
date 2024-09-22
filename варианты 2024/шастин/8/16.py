import sys
sys.setrecursionlimit(10000)
def f(n):
    if n > 10000:
        return n
    if n < 10000:
        return 5 * f(n + 3)

print(f(4625) / f(4640))