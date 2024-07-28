import sys
sys.setrecursionlimit(10000)
def f(n):
    if n >= 10000:
        return n
    if n < 10000 and n % 6 == 0:
        return n // 6 + f(n // 6 + 2)
    if n < 10000 and n % 6 != 0:
        return n + f(n + 2)

print(f(264) - f(7))