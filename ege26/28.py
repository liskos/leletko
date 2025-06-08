file = open("26data/26-J3.txt")
s,n = map(int,file.readline().split())
print(s,n)
a = [int(x) for x in file]
a.sort(reverse=True)
print(a)
b = []
for x in a:
    if sum(b) + x <= s:
        b.append(x)

print(len(b), min(b))