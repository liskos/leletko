file = open("26data/26-J3.txt")
s,n = map(int,file.readline().split())
print(s,n)
a = [int(x) for x in file]
a.sort(reverse=True)
print(a)
b = []
while sum(b) + a[0] <= s:
    b.append(a.pop(0))

while sum(b) <= s:
    m = [x for x in a if sum(b)+x <= s]
    if m:
        b.append(max(m))
    else:
        break

print(len(b), min(b))