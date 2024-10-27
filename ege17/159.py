a = [int(x) for x in open("17data/17-3.txt")]
r = []
for i in range(len(a) - 1):
    if (a[i] + a[i + 1]) % 3 == 0 and (a[i] + a[i + 1]) % 6 != 0 and str(a[i] * a[i + 1])[-1] == "8":
        r.append(a[i] + a[i + 1])
print(len(r), max(r))