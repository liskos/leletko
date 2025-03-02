a =[int(x) for x in open("17.txt")]
m = max([x for x in a if len(str(abs(x))) == 4])**3
r = []
for i in range(len(a) - 2):
    k = 0
    if str(a[i])[-1] in "35":
        k += 1
    if str(a[i+1])[-1] in "35":
        k += 1
    if str(a[i+2])[-1] in "35":
        k += 1
    if k > 1 and a[i] * a[i+1] * a[i+2] <= m:
        r.append(a[i] + a[i+1] + a[i+2])

print(len(r), max(r))