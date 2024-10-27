a = [int(x) for x in open("17data/17-3.txt")]
r = []
k = 0
for i in range(len(a) - 2):
    if a[i] < a[i + 1] < a[i + 2]:
        k += 1
        m = max(a[i], a[i + 1], a[i + 2])
        mi = min(a[i], a[i+1], a[i+2])
        r.append(m - mi)
print(len(r), min(r))