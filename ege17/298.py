def f(n):
    k = 0
    for i in range(len(str(n))):
        if int(str(n)[i]) * 197 == n:
            k = k + 1
    return k

a = [int(x) for x in open("17data/17-298.txt")]
c = []
m = max([x for x in a if x % 197 == 0])
for i in range(len(a)- 1):
    if (f(a[i]) == 1 and f(a[i+1]) != 1) or (f(a[i]) != 1 and f(a[i+1]) == 1) and a[i] + a[i+1] < m:
        c.append(a[i]+a[i+1])
print(len(c), max(c))
