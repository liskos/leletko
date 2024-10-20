a = [int(x) for x in open("17data/17-1.txt")]
sr = sum(a) / len(a)
b = []
for i in range(len(a) - 1):
    if (a[i] %17 == 0 or a[i + 1] % 17 == 0) and (a[i] > sr or a[i + 1] > sr):
        b.append(sum(a[i:i+2]))
print(len(b), max(b))
