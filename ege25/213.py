def f(n):
    b = ""
    while n> 0:
        b =b + str(n%8)
        n = n // 8
    return b[::-1]


import fnmatch
a = int("114", 8)
print(a)
for i in range(a,10**9,a):
    if fnmatch.fnmatch(f(i),"1?345?700"):
        print(i,i//a)