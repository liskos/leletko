file = open("26data/26-58.txt")
s,n = map(int,file.readline().split())
print(s,n)
a = [int(x) for x in file]
a.sort()
c = {x for x in a}
b = []
for x in c:
    if a.count(x) >= 2 and sum([x[0] for x in b]) + x*a.count(x) <= s:
        b.append([x*a.count(x),a.count(x)])
k = b[-1][1]
print(b)
b = b[:-1]
mm = max([x for x in c if x * k + sum([x[0] for x in b]) <= s])
b.append([mm*k,k])
print(mm,max([x[1] for x in b]))
