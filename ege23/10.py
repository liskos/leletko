a = [0] * 14
a[1] = 1
for i in range(2, 14):
    a[i] += a[i-2]
    a[i] += a[i-1]
    if i % 4 == 0:
        a[i] += a[i//4]
print(a[13])