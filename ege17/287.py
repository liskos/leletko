def pr(n):
    b = ""
    while n > 0:
        b = b + str(n % 3)
        n = n // 3
    return b[::-1]

def f(n):
    n = int(n)
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s


a = [int(x) for x in open("17data/17-282.txt")]
c = []
d = max([x for x in a if x % 11 == 0])
for i in range(len(a)- 1):
    if f(pr(a[i])) == f(pr(d)) or f(pr(a[i+1])) == f(pr(d)):
        c.append(a[i] + a[i+1])
print(len(c), min(c))