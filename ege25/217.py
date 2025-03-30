import fnmatch

def su(n):
    n = int(n)
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s

def f(n):
    b = ""
    while n > 0:
        b = b + str(n % 7)
        n = n // 7
    return b[::-1]

for i in range(1,2*10**9+1):
    if fnmatch.fnmatch(str(i), "1*586?6") and f(i) == f(i)[::-1]:
        print(i, su(f(i)))