def f(n):
    if n < sr:
        return 1
    else:
        return 0

def d(n):
    if str(n).count("5") >= 1:
        return 1
    else:
        return 0


a = [int(x) for x in open("17data/17-1.txt")]
r = []
sr = sum(a) / len(a)
for i in range(len(a)- 2):
    if (f(a[i]) + f(a[i+1]) + f(a[i+2]) >= 2) and ((d(a[i]) + d(a[i+1]) + d(a[i+2])) >= 2):
        r.append(a[i] + a[i+1] + a[i+2])

print(len(r), max(r))