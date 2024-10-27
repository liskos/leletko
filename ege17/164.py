a = [int(x) for x in open("17data/17-3.txt")]
r = []
k = 0
for i in range(len(a) - 2):
    if (a[i] * a[i + 1] * a[i + 2]) % 7 == 0 and str(a[i] + a[i + 1] + a[i + 2])[-1] == "5":
        k += 1
        r.append(a[i]+a[i+1]+a[i+2])
print(len(r), max(r))