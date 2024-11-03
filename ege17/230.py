a = [int(x) for x in open("17data/17-1.txt")]
r = []
sr = sum(a) / len(a)
for i in range(len(a)- 2):
    if (a[i] < sr or a[i+1] < sr or a[i+2] < sr) and (abs(a[i]) % 10 == 6 or abs(a[i+1]) % 10 == 6 or abs(a[i+2]) % 10 == 6):
        r.append(a[i] + a[i+1] + a[i+2])

print(len(r), max(r))