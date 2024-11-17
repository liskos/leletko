a = [0] * 25
a[1] = 1
for i in range(2, 25):
    a[i] += a[i-2]
    if i % 2 == 0:
        a[i] += a[i//2]
print(a[24])