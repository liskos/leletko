a = [int(x) for x in open("17data/17-1.txt")]
r = []
sr = sum(a) / len(a)
for i in range(len(a)- 1):
    if (a[i] > sr and a[i+1] > sr) and abs(a[i] + a[i+1]) % 100 == 31:
        r.append(a[i] + a[i+1])

print(len(r), max(r))