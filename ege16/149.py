import sys
sys.setrecursionlimit(1000000)
def f(n, m):
    if m > n:
        return 0
    if m <= n and n % m == 0:
        return 1 + f(n, m + 1)
    if m <= n and n % m != 0:
        return f(n, m + 1)

print(f(107864, 3))