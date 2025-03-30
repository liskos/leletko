import fnmatch

def f(n):
    s = 0
    while n>0:
        s = s + n % 10
        n = n // 10
    return s

for i in range(1,10**10+1):
    if f(i) % 11 == 0 and fnmatch.fnmatch(str(i),"17*023?9"):
        print(i, f(i)//11)