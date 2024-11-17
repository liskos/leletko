a = [0] * 37
a[12] = 1
for i in range(13, 37):
    a[i] += a[i-1]
    a[i] += a[i-10]
print(a[36], a)