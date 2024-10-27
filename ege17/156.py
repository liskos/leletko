a = [int(x) for x in open("17data/17-2.txt")]
r = []
m = max(a)
k = 0
for i in range(len(a) - 1):
    if a[i] == m:
        k += 1
        r.append(i)

print(k)
print(r[0] + 1)
print(m)