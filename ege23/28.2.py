a = [0] * 21
a[7] = 1
for i in range(8, 21):
    a[i] = a[i-1] + a[i-3]
print(a[20])
print(a)