a = [int(x) for x in open("17data/17-3.txt")]
r = []
k = 0
for i in range(len(a) - 2):
    if a[i] % 12 == 0 or a[i + 1] % 12 == 0 or a[i + 2] % 12 == 0:
        if a[i] % 3 == 0 and a[i + 1] % 3 == 0 and a[i + 2] % 3 == 0:
            k += 1
            r.append((a[i]+a[i+1]+a[i+2])/ 3)
print(len(r), min(r))