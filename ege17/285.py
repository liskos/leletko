def f(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s


a = [int(x) for x in open("17data/17-282.txt")]
c = []
d = min([x for x in a if x % 37 == 0])
for i in range(len(a)- 1):
    if f(a[i]) == f(d) or f(a[i+1]) == f(d):
        c.append(a[i] + a[i+1])
print(len(c), min(c))