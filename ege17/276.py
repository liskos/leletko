a = [int(x) for x in open("17data/17-276.txt")]
c = []
for i in range(len(a)- 2):
    s = sorted(a[i:i+3])
    k1 = s[1] / s[0]
    k2 = s[2] / s[1]
    if k1 == k2 and k1 > 1:
        c.append(k1**2)
print(len(c), max(c))