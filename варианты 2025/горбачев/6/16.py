import sys
sys.setrecursionlimit(1000000)
def f(n):
    if n < 52:
        return n
    if n >= 52:
        return 3*f(n-2)-n

print(f(15127)//f(15099))
