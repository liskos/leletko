import sys
sys.setrecursionlimit(100000)

def f(n):
    if n < 100:
        return n
    if n >= 100:
        return n + f(n-2)

print(f(66666) / f(777))