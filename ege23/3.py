a = [0] * 19
a[1] = 1
for i in range(2, 19):
    a[i] = a[i-1]
    if i % 2 == 0:
        a[i] += a[i//2]
    if i % 3 == 0:
        a[i] += a[i//3]
print(a[18])