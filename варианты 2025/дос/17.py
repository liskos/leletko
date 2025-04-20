a = [int(x) for x in open("17.txt")]
s = sum([x for x in a if x < 0 ])
r =[]
for i in range(len(a)-2):
    if (max(a[i],a[i+1],a[i+2]) * min(a[i],a[i+1],a[i+2])) > s:
        r.append(a[i]+a[i+1]+a[i+2])

print(len(r),max(r))