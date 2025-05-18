file = open("26data/26-k6.txt")
n,k = map(int,file.readline().split())
a = [x.split() for x in file]
b = []
for x in a:
    b.append([int(x[0]),int(x[1])])
c = []
for x in b:
    c.append([x[1]/x[0],x[0],x[1]])
c.sort()
print(max([x[2] for x in c[:k]]))
var = [x[::-1][1] for x in c if x[0] == max(c[:k])[0]]
var.sort(reverse=True)
km = len([x for x in c[:k] if x[0] == max(c[:k])[0]])
print(sum(var[:km]) + sum([x[1] for x in c[:k-km]]))

