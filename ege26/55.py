file = open("26data/26-55.txt")
n,s = map(int,file.readline().split())
print(n)
print(s)
a = [int(x) for x in file]
a.sort(reverse=True)
b = []
k = 0
mm = []
while len(a) > 0:
    while len(a) > 0 and sum(b) + a[0] <= s:
        b.append(a.pop(0))
    if a and len([x for x in a if sum(b) + x <= s]) > 0:
        m = max([x for x in a if sum(b) + x <= s])
        for x in range(len(a)):
            if a[x] == m:
                a.pop(x)
                break
    k += 1
    mm.append(sum(b))
    b = []

print(k,mm[-1])

