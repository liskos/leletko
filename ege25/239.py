import fnmatch

def d(n):
    r = set()
    k = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            if i % 2 == 0:
                r.add(i)
            if n // i % 2 == 0:
                r.add(n//i)
    return r

k = 0
for i in range(65000,10**10):
    if k == 7:
        break
    if fnmatch.fnmatch(str(i), "6*97*5?") and len(d(i)) >= 4:
        print(i,sum(d(i)))
        k += 1
