a = [0] * 17
a[1] = 1
for i in range(2, 17):
    a[i] = a[i-1]
    if i % 2 == 0:
        a[i] += a[i//2]
print(a[16])