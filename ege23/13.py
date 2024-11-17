a = [0] * 50
a[5] = 1
for i in range(6, 50):
    a[i] += a[i-1]
    if i % 3 == 0:
        a[i] += a[i//3]
print(a[49], a)