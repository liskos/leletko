import fnmatch

def devided(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a

k = 0
for i in range(1,10**10):
    if k == 7:
        break
    if i % 6 == 0 and i % 7 == 0 and i % 8 == 0 and fnmatch.fnmatch(str(i), "?6*6*?6"):
        print(i, sum(devided(i)))
        k += 1
