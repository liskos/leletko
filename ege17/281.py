def f(a):
    k1 = a[1] - a[0]
    k2 = a[2] - a[1]
    k3 = a[4] / a[3]
    k4 = a[5] / a[4]
    if k1 == k2 and k1 > 0 and k3 == k4 and k3 > 1 and float(k2) == k3:
        return True
    else:
        return False
a = [int(x) for x in open("17data/17-281.txt")]
c = []
for i in range(len(a)- 5):
    if f(a[i:i+6]) or f(a[i+3:i+6]+a[i:i+3]):
        c.append(sum(a[i:i+6]))

print(len(c), max(c))