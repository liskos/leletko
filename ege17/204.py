def f(x):
    return x >= 0 and abs(x) % 10 == 9

a = [int(x) for x in open("17data/17-204.txt")]
r = []
for i in range(len(a)- 2):
    if not f(a[i]) and f(a[i+1]) and not f(a[i+2]):
        s = a[i] + a[i+1] + a[i+2]
        r.append(s)
print(len(r), max(r))