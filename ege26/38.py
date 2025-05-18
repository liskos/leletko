file = open("26data/26-j9.txt")
s,n = map(int,file.readline().split())
a = [int(x) for x in file]
a.sort(reverse=True)
b = []
c = 0
for i in range(n):
    if sum(b) + a[i] <= s:
        b.append(a[i])
        c = a[i]
    if sum(b) + a[-(i+1)] <= s:
        b.append(a[-(i+1)])
        c = a[-(i+1)]

print(len(b), c)

