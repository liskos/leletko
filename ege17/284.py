a = [int(x) for x in open("17data/17-282.txt")]
c = []
d = max([x for x in a if x % 41 == 0])
for i in range(len(a)- 1):
    if a[i] + a[i+1] < d:
        c.append(a[i] + a[i+1])
print(len(c), max(c))