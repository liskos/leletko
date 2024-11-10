def f(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s

a = [int(x) for x in open("17data/17-299.txt")]
c = []
m = sum([f(x) for x in a if x % 50 == 0])
for i in range(len(a)- 2):
    if (a[i] == f(a[i+1]) or a[i] == f(a[i+2])) or (a[i+1] == f(a[i]) or a[i] == f(a[i+2])) or (a[i+2] == f(a[i+1]) or a[i] == f(a[i])):
        if a[i] + a[i+1] + a[i+2] < m:
            c.append(sum(a[i:i+3]))
print(len(c), max(c))
