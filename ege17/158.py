a = [int(x) for x in open("17data/17-1.txt")]
r = []
k = 0
for i in range(len(a) - 1):
    d = 1
    while a[i] > a[i + 1]:
        d += 1
        i += 1
    if d == 7:
        r.append(d)

print(max(r), len(r))