a = [int(x) for x in open("17data/17-271.txt")]
sr = sum(a) / len(a)
b = []
c = []
for i in range(len(a)- 1):
    if int(str(a[i])[-1]) + int(str(a[i+1])[-1]) == 7:
        b.append(a[i]+a[i+1])
        if a[i] < sr and a[i+1] < sr:
            c.append(a[i]+a[i+1])

print(len(b), max(c))
