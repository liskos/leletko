a = [int(x) for x in open("17.txt")]
m = min([x for x in a if x > 0 and x % 2025 == 0])
r = []
for i in range(len(a)- 3):
    if a[i] > 0 and a[i+3] > 0 and abs(a[i+1] - a[i+2]) <= m:
        r.append(a[i]+a[i+1]+a[i+2]+a[i+3])

print(len(r), min(r))