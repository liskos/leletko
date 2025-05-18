file = open("26data/26-45.txt")
n = int(file.readline())
a = [int(x) for x in file]
c = [x for x in a if x % 2 == 0]
nc = [x for x in a if x % 2 != 0]
k = 0
msr = 0
print("1")
for x in range(len(c)-1):
    for y in range(x+1,len(c)):
        if (c[x] + c[y])//2 in a:
            k += 1
            msr = max(msr,(c[x] + c[y])//2)

print("2")
for x in range(len(nc)-1):
    for y in range(x+1,len(nc)):
        if (nc[x] + nc[y])//2 in a:
            k += 1
            msr = max(msr,(nc[x] + nc[y])//2)
print(k)
print(msr)