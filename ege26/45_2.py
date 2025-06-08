file = open("26data/26-45.txt")
import time
t1 = time.time()
n = int(file.readline())
a = {int(x) for x in file}
c = [x for x in a if x % 2 == 0]
nc = [x for x in a if x % 2 != 0]
k = 0
msr = 0
for x in range(len(c)-1):
    for y in range(x+1,len(c)):
        s = (c[x] + c[y])//2
        if s in a:
            k += 1
            msr = max(msr,s)

for x in range(len(nc)-1):
    for y in range(x+1,len(nc)):
        s = (nc[x] + nc[y])//2
        if s in a:
            k += 1
            msr = max(msr,s)
print(k)
print(msr)
print(time.time()-t1)