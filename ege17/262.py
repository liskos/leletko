a = [int(x) for x in open("17data/17-257.txt")]
s = [x for x in a if x % 2 == 1]
m = max(a)
h = max(s) + min(s)
b = []
for i in range(len(a)- 1):
    if (a[i] + a[i+1] % 2 == 0) and (a[i] + a[i+1] > h):
        b.append(a[i] + a[i+1])

print(h)