a = [0] * 19
a[1] = 1
for i in range(2, 19):
    a[i] += a[i-3]
    a[i] += a[i-1]
    if i % 4 == 0:
        a[i] += a[i//4]
print(a[18])