import fnmatch

def d(n):
    r = set()
    k = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            if i % 2 != 0:
                r.add(i)
            if n // i % 2 != 0:
                r.add(n//i)
    return r

k = 0
for i in range(10**7+1,1,-1):
    if k == 7:
        break
    if i % 217 == 0 and fnmatch.fnmatch(str(i), "14?4*"):
        print(i,sum(d(i)))
        k += 1
