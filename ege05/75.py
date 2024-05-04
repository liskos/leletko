def f(n):
    a = [int(x) for x in str(n)]
    a[0] += 3
    a[1] += 6
    a[2] += 5
    a = sorted(a)
    a = [str(x) for x in a]
    return "".join(a)

for i in range(100, 1000):
    if f(i) == "51014":
        print(i)