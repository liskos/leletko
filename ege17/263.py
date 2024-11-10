def f(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s

a = [int(x) for x in open("17data/17-243.txt")]
s = [f(x) for x in a if x % 33 == 0]
b = []
for i in range(len(a)- 1):
    if a[i] > sum(s) or a[i+1] > sum(s):
        b.append(a[i] + a[i+1])

print(len(b), min(b))