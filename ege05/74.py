def f(n):
    a =[ int(x) for x in str(n)]
    a[0] += 7
    a[1] += 1
    a[2] += 4
    a = sorted(a)
    a = [str(x) for x in a ]
    return "".join(a)

for i in range(100, 1000):
    if f(i) == "91012":
        print(i)
        break