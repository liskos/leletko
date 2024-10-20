a = [int(x) for x in open("17data/17-243.txt")]
m = max(x for x in a if x % 119 == 0)
b = []
for i in range(len(a)- 1):
    if (a[i] > m or a[i+1] > m) and (abs(a[i]) % 100 == 21 or abs(a[i + 1]) % 100 == 21):
        b.append(a[i] + a[i+1])

print(len(b), min(b))