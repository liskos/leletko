import sys
sys.setrecursionlimit(10000)
def f(n):
    if n >= 10000:
        return n
    if n < 10000 and n % 3 == 0:
        return n + f(n // 3)
    if n < 10000 and n % 3 != 0:
        return 2 * n + f(n + 3)

print(f(999) - f(46))