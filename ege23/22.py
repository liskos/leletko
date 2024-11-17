a = [0] * 47
a[24] = 1
for i in range(25, 47):
    a[i] += a[i-1]
    if (i - 11) % 10 != 9 and (i - 11) % 100 < 90:
        a[i] += a[i-11]
    if (i - 11) % 100 > 89:
        a[i] += 0
    if i % 10 == 9:
        a[i] += a[i-10]
print(a[46], a)