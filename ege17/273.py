a = [int(x) for x in open("17data/17-273.txt")]
m = max(a)
b = []
for i in range(len(a)- 2):
    if a[i] + a[i+1] + a[i+2] < m:
        b.append(a[i])
        b.append(a[i+1])
        b.append(a[i+2])

print(len(b), max(b) + min(b))