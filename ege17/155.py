a = [int(x) for x in open("17data/17-1.txt")]
r = []
for i in range(1, len(a) - 1):
    if a[i-1] > a[i] < a[i + 1]:
        r.append(a[i])

print(len(r), max(r))