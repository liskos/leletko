def f(n):
    a = str(n)
    d = int(a[0]) * int(a[1])
    c = int(a[0]) * int(a[2])
    s = int(a[0]) * int(a[3])
    m = sorted([d,c,s])
    return str(m[1]) + str(m[2])

print(f(2345))
for i in range(1000,10000):
    if f(i) == "5472":
        print(i)
        break