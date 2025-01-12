def f(n):
    a = str(n)
    d = int(a[0]) * int(a[1])
    c = int(a[0]) * int(a[2])
    s = int(a[0]) * int(a[3])
    m = max(d,c,s)
    sr = d+s+c - m - min(d,c,s)
    return str(sr) + str(m)

print(f(2345))
for i in range(1000,10000):
    if f(i) == "5472":
        print(i)
        break