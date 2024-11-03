a = [int(x) for x in open("17data/17-243.txt")]
r = []
m = []
for i in range(len(a)):
    if a[i] % 171 == 0:
        m.append(a[i])

for i in range(len(a)- 1):
    if (a[i] < max(m) or a[i+1] < max(m)) and (a[i] % 2 != 0 or a[i+1] % 2 != 0):
        r.append(a[i] + a[i+1])

print(len(r), max(r))