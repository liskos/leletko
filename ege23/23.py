a = [0] * 50
a[26] = 1
for i in range(27, 50):
    a[i] += a[i-1]
    if i % 10 != 0:
        a[i] += a[i-11]
    if i % 10 == 9:
        a[i] += a[i-10]
print(a[49], a)