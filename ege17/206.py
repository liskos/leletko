a = [int(x) for x in open("17data/17-205.txt")]
r = []
for i in range(len(a)- 1):
    if (a[i] % 7 == 0 or a[i+1] % 7 == 0) and (a[i] + a[i+1]) % 5 == 0:
        r.append(a[i] + a[i+1])

print(len(r), max(r))