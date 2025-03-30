import fnmatch

def devided(n):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a

k = 0
for i in range(10**7+1,1,-1):
    if k == 5:
        break
    if fnmatch.fnmatch(str(i),"9?*55*7"):
        print(i,sum(devided(i)) % 21)
        k += 1

