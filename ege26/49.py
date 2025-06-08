file = open("26data/26-49.txt")
n = int(file.readline())
print(n)
r= []
a = [int(x) for x in file]
a.sort()
for x in range(len(a)-1):
    for y in range(x,len(a)):
        if (a[x] + a[y]) % 2 == 0 and a[x] != a[y]:
            sr = (a[x] + a[y])//2
            if sr < a[n//2]:
                r.append(sr)


print(len(r),max(r))


