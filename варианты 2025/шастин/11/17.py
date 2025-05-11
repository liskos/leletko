a = [int(x) for x in open("17.txt")]
m = max([x for x in a])
r = []
for i in range(len(a)-2):
    p = []
    o = []
    for x in a[i:i+3]:
        if x >=0:
            p.append(x)
        else:
            o.append(x)
    if abs(sum(o)) <= sum(p) and str(a[i] * a[i+1] * a[i+2])[-1] == str(m)[-1]:
        r.append(abs(a[i]*a[i+1]*a[i+2]))

print(len(r), max(r))