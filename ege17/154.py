a = [int(x) for x in open("17data/17-1.txt")]
r = []
d = []
k = 0
for i in range(len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        k += 1
        r.append(i)
    if len(r) > 1:
        x = abs(r[-1] - r[-2])
        d.append(x)
print(k, min(d))
print(r)