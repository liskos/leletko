a = [int(x) for x in open("17data/17-292.txt")]
c = []
for i in range(len(a)- 2):
    if abs(a[i] % 17 - a[i+1] % 17) == a[i] % 4 + a[i+1] % 4:
        c.append(a[i]+a[i+1])
print(len(c), min(c))