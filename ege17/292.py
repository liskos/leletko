def f(n):
    b = ""
    while n > 0:
        b = b + str(n%6)
        n = n // 6
    return len(b)


a = [int(x) for x in open("17data/17-292.txt")]
c = []
for i in range(len(a)- 1):
    if a[i] % 6 + a[i+1] % 6 == a[i] % 11 + a[i+1] % 11:
        c.append(a[i]+a[i+1])

print(len(c), max(c))