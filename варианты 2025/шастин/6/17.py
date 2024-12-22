a = [int(x) for x in open("17.txt")]
m = min([x for x in a])
r = []
for i in range(len(a)- 2):
    b = str(a[i]) + str(a[i+1]) + str(a[i+2])
    if b.count("-") >= 2 and str(a[i] + a[i+1] + a[i+2])[-1] == str(m)[-1]:
        r.append(abs(a[i]+a[i+1]+a[i+2]))

print(len(r), max(r))