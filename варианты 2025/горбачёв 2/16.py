import sys
sys.setrecursionlimit(10000)
def f(n):
    if n == 3:
        return 3
    if n > 3:
        return (3+n) * f(n-1)

print((f(3076)// 17 + f(3075) // 45)/f(3072))