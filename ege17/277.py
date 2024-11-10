def f(n):
    b = ""
    while n > 0:
        b = b + str(n % 3)
        n = n // 3
    return b.count("2")


a = [int(x) for x in open("17data/17-277.txt")]
c = []
d = [f(abs(x)) for x in a if abs(x) % 60 == 0]
for i in range(len(a)- 1):
    if a[i] > sum(d) or a[i+1] > sum(d):
        c.append(a[i] + a[i+1])
print(len(c), max(c))