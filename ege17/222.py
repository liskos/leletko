def f(n):
    return n % 7 == 0 and n % 3 != 0 and n % 11 != 0 and n % 13 != 0

a = [int(x) for x in open("17data/17-4.txt")]
r = []
sr = sum(a) / len(a)
for i in range(len(a)- 1):
    if (a[i] < sr or a[i+1] < sr) and (f(a[i]) or f(a[i+1])):
        r.append(a[i] + a[i+1])

print(len(r), min(r))