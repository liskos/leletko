import sys
sys.setrecursionlimit(10000)
def f(n):
    if n <= 110:
        return n
    if n >= 110:
        return (n-7) * f(n-8)

print((f(74914) - f(74898)) / (16* f(74890)))