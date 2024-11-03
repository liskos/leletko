a = [int(x) for x in open("17data/17-4.txt")]
r = []
sr = sum(a) / len(a)
for i in range(len(a)- 1):
    if (a[i] < sr or a[i+1] < sr) and (str(a[i]).count("5") == 0 or str(a[i+1]).count("5") == 0):
        r.append(a[i] + a[i+1])

print(len(r), min(r))