a = [int(x) for x in open("17data/17-257.txt")]
s = max([x for x in a if x % 2 != 0])
b = []
for i in range(len(a)- 1):
    if 2 * (a[i] + a[i+1]) > s:
        b.append(a[i] + a[i+1])

print(len(b), min(b))