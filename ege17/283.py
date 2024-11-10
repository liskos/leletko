a = [int(x) for x in open("17data/17-282.txt")]
c = []
d = max([x for x in a if x % 13 == 0])
for i in range(len(a)- 1):
    if a[i] % d == 0 or a[i+1] % d == 0:
        c.append(a[i] + a[i+1])
print(len(c), min(c))