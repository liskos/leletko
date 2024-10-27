a = [int(x) for x in open("17data/17-5.txt")]
r = []
k = 0
for i in range(len(a) -1):
    if a[i] % 2 == 0 or a[i+1] % 2 == 0:
        r.append(a[i] + a[i + 1])
print(len(r), max(r))