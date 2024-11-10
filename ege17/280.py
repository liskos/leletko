def f(n):
    b = ""
    while n > 0:
        b = b + str(n % 8)
        n = n // 8
    return b.count("7")


a = [int(x) for x in open("17data/17-278.txt")]
c = []
d = [f(x) for x in a]
for i in range(len(a)- 1):
    if a[i] > sum(d) and a[i+1] > sum(d):
        c.append(a[i] + a[i+1])
print(len(c), min(c))