a = [0] * 18
a[1] = 1
for i in range(2, 18):
    a[i] = a[i-1]
    if i % 2 == 0:
        a[i] += a[i//2]
    if i % 4 == 0:
        a[i] += a[i//4]
print(a[17])