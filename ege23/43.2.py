a = [0] * 21
a[3] = 1
for i in range(4, 13):
    a[i] = a[i-1] + a[i-3]
b = [0] * 21
b[12] = a[12]
for i in range(13, 21):
    b[i] = b[i-1] + b[i-3]

print(b[20])