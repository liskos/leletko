a = [int(x) for x in open("17data/17-1.txt")]
r = []
sr = sum(a) / len(a)
for i in range(len(a)- 2):
    if a[i] < sr or a[i+1] < sr or a[i+2] < sr:
        k = 0
        if a[i] % 7 == 0:
            k += 1
        if a[i+1] % 7 == 0:
            k += 1
        if a[i+2] % 7 == 0:
            k += 1
        if k >= 2:
            r.append(a[i] + a[i+1] + a[i+2])

print(len(r), max(r))