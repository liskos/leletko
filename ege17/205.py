a = [int(x) for x in open("17data/17-205.txt")]
r = []
for i in range(len(a)- 1):
    c = a[i] - a[i+1]
    if c % 2 == 0 and c % 37 == 0:
        r.append(a[i] + a[i+1])

print(len(r), max(r))