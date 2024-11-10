def s(n):
    s = 1
    while n > 0:
        s = s * n%10
        n = n // 10
    return s


a = [int(x) for x in open("17data/17-294.txt")]
c = []
m = max(a)
for i in range(len(a)- 1):
    if s(a[i]+a[i+1]) > 0 and (a[i] + a[i+1]) % s(a[i]+a[i+1]) == 0 and (a[i] + a[i+1]) < m:
        c.append(a[i]+a[i+1])
print(len(c), max(c))