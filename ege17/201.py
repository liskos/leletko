def f(x):
    return len(str(abs(x))) == 3 and x >= 0 and x % 2 != 0

a = [int(x) for x in open("17data/17-199.txt")]
r = []
for i in range(len(a)- 2):
    if not f(a[i]) and f(a[i+1]) and not f(a[i+2]):
        s = a[i] + a[i+1] + a[i+2]
        r.append(s)
print(len(r), max(r))