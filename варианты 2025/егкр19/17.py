a = [int(x) for x in open("17.txt")]
m = min([x for x in a if x > 0 and len(str(x)) == 4 and x % 10 == 6])
r = []
for i in range(len(a)-2):
    k = 0
    if len(str(abs(a[i]))) == 4 and abs(a[i]) % 10 == 6:
        k += 1
    if len(str(abs(a[i+1]))) == 4 and abs(a[i+1]) % 10 == 6:
        k += 1
    if len(str(abs(a[i+2]))) == 4 and abs(a[i+2]) % 10 == 6:
        k += 1
    if k == 1 and (a[i]+a[i+1]+a[i+2]) <= m:
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r), max(r))