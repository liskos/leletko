a = [int(x) for x in open("17data/17-243.txt")]
m = max(x for x in a if x % 211 == 0)
b = []
for i in range(len(a)- 1):
    if (a[i] > m or a[i+1] > m) and (str(a[i]).count("1") > 0 or str(a[i+1]).count("1") > 0):
        b.append(a[i] + a[i+1])

print(len(b), min(b))