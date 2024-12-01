a =[int(x) for x in open("17.txt")]
m = min([x for x in a if str(x)[-1] == '8'])
r = []
for i in range(len(a) - 1):
    if (a[i] % 16 == m and a[i+1] % 16 != m) or (a[i] % 16 != m and a[i+1] % 16 == m):
        r.append(a[i] + a[i+1])

print(len(r), max(r))