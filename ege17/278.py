def f(n):
    b = ""
    while n > 0:
        b = b + str(n % 5)
        n = n // 5
    return b.count("3")


a = [int(x) for x in open("17data/17-278.txt")]
c = []
d = [f(x) for x in a if x % 32 == 0]
for i in range(len(a)- 2):
    if a[i] > sum(d) or a[i+1] > sum(d) or a[i+2] > sum(d):
        c.append(a[i] + a[i+1] + a[i+2])
print(len(c), max(c))