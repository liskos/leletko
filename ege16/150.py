import sys
sys.setrecursionlimit(10000)
def f(n):
    if n <= 3:
        return n - 1
    if n > 3 and n % 2 == 0:
        return n + f(n // 3)
    if n > 3 and n % 2 != 0:
        return f(n - 1) * n + f(n - 2)

print(f(4952) + 2 * f(4958) + f(4964))