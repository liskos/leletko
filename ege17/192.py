def f(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s

a = [int(x) for x in open("17data/17-7.txt")]
r = []
k = 0
for i in range(len(a) -2):
    if f(a[i]) == 3:
        r.append(a[i])
print(len(r), max(r))