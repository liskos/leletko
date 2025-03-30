a = [int(x) for x in open("17.txt")]
m = max([x for x in a if abs(x) % 36 == 0])
r = []
for i in range(len(a)-2):
    k = 0
    if a[i] >0 or abs(a[i]) % 100 == 36:
        k += 1
    if a[i+1] >0 or abs(a[i+1]) % 100 == 36:
        k += 1
    if a[i+2] >0 or abs(a[i+2]) % 100 == 36:
        k += 1
    if k >= 2 and sum(a[i:i+3]) <= m:
        r.append(sum(a[i:i+3]))

print(len(r), min(r))