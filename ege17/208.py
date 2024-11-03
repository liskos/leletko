a = [int(x) for x in open("17data/17-205.txt")]
r = []
for i in range(len(a)- 1):
    if (abs(a[i]) % 100 == 17 or abs(a[i+1]) % 100 == 17) and (a[i] + a[i+1]) % 2 == 0:
        r.append(a[i] + a[i+1])

print(len(r), max(r))