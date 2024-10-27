a = [int(x) for x in open("17data/17-3.txt")]
r = []
k = 0
for i in range(len(a) - 1):
    if a[i] % 2 != a[i+1] % 2 and (a[i] % 4 == 0 or a[i+1] % 4 == 0) and (a[i] % 11 == 0 or a[i+1] % 11 == 0):
        k += 1
        r.append(a[i] + a[i + 1])
print(k, max(r))