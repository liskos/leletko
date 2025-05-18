import sys
sys.setrecursionlimit(100000)
def f(n):
    if n < 6:
        return n
    if n >= 6:
        return (3*n-2) * f(n-5)


print( (f(20568)- 51702 * f(20563))/f(20553) )