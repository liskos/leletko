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
    while n>0:
        b = b + str(n%9)
        n = n // 9
    return b[::-1]

for i in range(1,10**9):
    if fnmatch.fnmatch(str(i), "3?458*3") and all(f(i)[x] >= f(i)[x+1] for x in range(len(f(i))-1)):
        print(i,su(f(i)))
