a = [int(x) for x in open("17data/17-205.txt")]
r = []
for i in range(len(a)- 1):
    if (a[i] % 10 == 7 or a[i+1] % 10 == 7) and abs(a[i] + a[i+1]) % 12 == 0:
        r.append(a[i] + a[i+1])

print(len(r), max(r))