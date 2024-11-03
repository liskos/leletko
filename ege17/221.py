def f(n):
    n = int(n)
    return n % 3 == 0 and n % 5 != 0 and n % 11 != 0 and n % 19 != 0

a = [int(x) for x in open("17data/17-1.txt")]
r = []
sr = sum(a) / len(a)
for i in range(len(a)- 1):
    if (a[i] < sr or a[i+1] < sr) and (f(a[i]) or f(a[i+1])):
        r.append(a[i] + a[i+1])

print(len(r), max(r))