a = [int(x) for x in open("17data/17-10.txt")]
r = []
for i in range(len(a) -2):
    m = max(a[i], a[i+1], a[i+2])
    mi = min(a[i], a[i+1], a[i+2])
    sr = a[i] + a[i+1] + a[i+2] - m - mi
    if m ** 2 == (mi ** 2 + sr ** 2):
        r.append(mi)

print(len(r), sum(r))
