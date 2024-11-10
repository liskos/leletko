def f(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s


a = [int(x) for x in open("17data/17-272.txt")]
b = [x for x in a if x >= 0]
sr = sum(b) / len(b)
c = []
for i in range(len(a)- 1):
    if a[i] > sr or a[i+1] > sr:
        c.append(max(f(a[i]), f(a[i+1])))

print(len(c), max(c))