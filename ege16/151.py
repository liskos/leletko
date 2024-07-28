import sys
sys.setrecursionlimit(10000)
def f(n):
    if n <= 10:
        return n
    if n >= 10000:
        return 1
    if 10 < n < 10000 and n % 2 == 0:
        return n % 10 + f(n + 2)
    if 10 < n < 10000 and n % 2 != 0:
        return f(n - 2) - (n - 1) % 10

print(f(4500) + f(5515))