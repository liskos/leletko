file = open("26data/26-51.txt")
n = int(file.readline())
print(n)
r = []
a = [int(x) for x in file]
a.sort()
print(a)
for x in range(len(a)-1):
    for y in range(x,len(a)):
        if (a[x] + a[y]) % 2 == 0 and y-x>=100+1 and a[x] != a[y]:
            r.append(a[x]+a[y])

print(len(r), max(r)//2)