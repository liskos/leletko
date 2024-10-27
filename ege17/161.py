a = [int(x) for x in open("17data/17-3.txt")]
r = []
k = 0
for i in range(len(a) - 1):
    if str(a[i] + a[i + 1])[-1] != "6" and (a[i] + a[i + 1]) % 2 == 0:
        k += 1
        r.append((a[i] + a[i + 1]) / 2)
print(k, max(r))