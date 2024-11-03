def f(n):
    b = ""
    while n > 0:
        b = b + str(n % 7)
        n = n // 7
    return b[::-1]

a = [int(x) for x in open("17data/17-10.txt")]
r = []
for i in range(len(a) -2):
    s = a[i] + a[i+1]
    if f(s) == f(s)[::-1]:
        r.append(int(f(s)))

print(len(r), max(r))
