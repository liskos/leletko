file = open("26data/26-53.txt")
n = int(file.readline())
print(n)
r = []
a = [int(x) for x in file]
for x in range(len(a)-1):
    for y in  range(x,len(a)):
        if a[x] % 2 == 0 and a[y] % 2 == 0 and a[x]!=a[y]:
            sr = (a[x]+a[y])//2
            if sr in a:
                r.append(sr)

print(len(r),min(r))