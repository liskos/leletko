a = [int(x) for x in open("17.txt")]
m = max([x for x in a]) / 2
r = []
for i in range(len(a) - 2):
    k = 0
    if "0" not in str(a[i]):
        k += 1
    if "0" not in str(a[i+1]):
        k += 1
    if "0" not in str(a[i+2]):
        k += 1
    if k >= 2 and (a[i] + a[i+1] + a[i+2]) < m:
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r), max(r))