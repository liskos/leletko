import sys
sys.setrecursionlimit(10000)
def f(n):
    if n <= 10:
        return 10
    if n > 10:
        return 7 * n * f(n-2)


print((f(9242) - f(9241))//(f(9240)//19))