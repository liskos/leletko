a = [int(x) for x in open("17.txt")]
r = []
for i in range(len(a) - 5):
    p1 = a[i] + a[i+1]
    p2 = a[i+2] + a[i+3]
    p3 = a[i+4] + a[i+5]
    if (p1 >= 0 and p2 >= 0 and p3 >= 0) and p2 > p1 and p2 > p3:
        r.append(a[i+2] * a[i+3])

print(len(r), min(r))