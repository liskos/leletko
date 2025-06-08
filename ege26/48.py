file = open("26data/26-48.txt")
n = int(file.readline())
print(n)
a = [int(x) for x in file]
r = []
for x in range(len(a)-1):
    for y in range(x,len(a)):
        if (a[x] + a[y]) % 2 == 0 and a[x] != a[y]:
            sr = (a[x] + a[y]) // 2
            if sr + 5 in a or sr - 5 in a:
                r.append([sr])

print(len(r),min(r)[0])
