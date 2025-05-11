file = open("26data/26-5.txt")
s,n = map(int,file.readline().split())
a = [int(x) for x in file]
a.sort()
b = []
while sum(b) + a[0] <= s:
    b.append(a.pop(0))
print(len(b))
a.append(b.pop(-1))
m = max([x for x in a if sum(b)+x <= s])
print(m)