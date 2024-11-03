a = [int(x) for x in open("17data/17-4.txt")]
r = []
sr = sum(a) / len(a)
for i in range(len(a)- 1):
    if (a[i] < sr and a[i+1] < sr) and (a[i] % 10 == 9 or a[i+1] % 10 == 9):
        r.append(a[i] + a[i+1])

print(len(r), max(r))