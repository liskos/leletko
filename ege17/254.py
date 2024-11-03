a = [int(x) for x in open("17data/17-243.txt")]
m = max(x for x in a if x % 151 == 0)
b = []
for i in range(len(a)- 1):
    if (a[i] > m or a[i+1] > m) and (hex(a[i]).count("3") >= 1 or hex(a[i+1]).count("3") >= 1):
        b.append(a[i] + a[i+1])

print(len(b), min(b))