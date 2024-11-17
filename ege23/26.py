a = [0] * 43
a[3] = 1
for i in range(4, 43):
    a[i] += a[i-3]
    if i % 2 == 0:
        a[i] += a[i//2]
print(a[42], a)