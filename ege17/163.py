def f(a, b):
     return (a % 2 != b % 2) and a % 4 == 0 and b % 11 == 0


a = [int(x) for x in open("17data/17-3.txt")]
r = []
for i in range(len(a) - 1):
    if f(a[i], a[i+1]) or f(a[i+1], a[i]):
        r.append(a[i] + a[i + 1])
print(len(r), max(r))