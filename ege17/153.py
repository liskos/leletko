a = [int(x) for x in open("17data/17-1.txt")]
r = []
k = 0
for i in range(len(a) - 1):
    if a[i] < a[i + 1]:
        k += 1
        d = abs(a[i] - a[i + 1])
        r.append(d)
print(k)
print(min(r))