a = [int(x) for x in open("17data/17-3.txt")]
r = []
k = 0
for i in range(len(a) - 3):
    if a[i] > a[i+1] > a[i+2] > a[i+3]:
        if a[i] - a[i+3] > 1000:
            r.append(a[i] + a[i+1] + a[i+2] + a[i+3])
print(len(r), min(r))