def f(a, b):
    return bin(a).count("1") > 5 and bin(b).count("1") % 2 == 0

a = [int(x) for x in open("17data/17-8.txt")]
r = []
k = 0
for i in range(len(a) - 1):
    if f(a[i], a[i+1]) or f(a[i+1], a[i]):
        r.append(a[i] + a[i+1])
print(len(r), max(r))