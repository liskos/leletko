a = [int(x) for x in open("17.txt")]

s = sum([x for x in a if len(str(abs(x))) == 4])

r = []
for i in range(len(a) - 2):
    t = a[i:i+3]
    g = [j for j in t if len(str(abs(j))) == 3]
    if len(g) == 2:
        if t[0] * t[1] * t[2] > s:
            r.append(t[0] * t[1] * t[2])

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