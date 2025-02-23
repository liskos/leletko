a = [int(x) for x in open("17.txt")]

s = sum([x for x in a if len(str(abs(x))) == 4])

r = []
for i in range(len(a) - 2):
    if ((len(str(abs(a[i]))) == 3) + (len(str(abs(a[i+1]))) == 3) + (len(str(abs(a[i+2]))) == 3)) == 2:
        if (a[i] * a[i+1] * a[i+2]) > s:
            r.append(a[i] * a[i+1] * a[i+2])

print(len(r), abs(min(r)))

b = []
for i in range(len(a) - 2):
    k = 0
    if len(str(abs(a[i]))) == 3:
        k += 1
    if len(str(abs(a[i+1]))) == 3:
        k += 1
    if len(str(abs(a[i+2]))) == 3:
        k += 1
    if k == 2 and ((a[i] * a[i+1] * a[i+2]) > s):
        b.append(a[i] * a[i+1] * a[i+2])

print(len(b), abs(min(b)))