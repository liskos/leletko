a = [0] * 34
a[10] = 1
for i in range(11, 34):
    a[i] += a[i-1]
    if i % 100 > 89:
        a[i] += a[i-9]
    else:
        a[i] += a[i-10]

print(a[33], a)