a = [int(x) for x in open("17data/17-257.txt")]
s = [x for x in a if x % 10 == 4]
d = max(s) + min(s)
b = []
for i in range(len(a)- 1):
    if a[i] + a[i+1] < d:
        b.append(a[i] + a[i+1])

print(len(b), max(b))
