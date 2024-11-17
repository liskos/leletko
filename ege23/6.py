a = [0] * 13
a[1] = 1
for i in range(2, 13):
    a[i] += a[i-2]
    a[i] += a[i-1]
    if i % 3 == 0:
        a[i] += a[i//3]
print(a[12])