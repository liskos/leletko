a = [int(x) for x in open("17.txt")]
k = len([ x for x in a if abs(x) % 2 == 0])
r = []
for i in range(len(a) - 1):
    if (a[i] > 0) == (a[i+1] > 0) and abs(a[i] - a[i+1]) <= k:
        r.append(a[i]+ a[i+1])

print(len(r), max(r))