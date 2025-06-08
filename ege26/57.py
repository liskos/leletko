file = open("26data/26-57.txt")
n,m = map(int,file.readline().split())
print(n,m)
a = [int(x) for x in file]
a.sort(reverse=True)
b = []
k = 0
while sum(a) >= m:
    while sum(b) + a[0] <= m:
        b.append(a.pop(0))
        if a and len([x for x in a if sum(b) + x >= m]) > 0:
            mm = min([x for x in a if sum(b) + x >= m])
            if mm - (m - sum(b)) >0:
                a.append(mm - (m - sum(b)))
            b.append(m-sum(b))
            k += len(b)-1
            for x in range(len(a)):
                if a[x] == mm:
                    a.pop(x)
                    break
    b = []
print(k)
print(len(a))
