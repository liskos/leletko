def f(n):
    a = [int(x) for x in str(n)]
    a[0] += 4
    a[1] += 9
    a[2] += 7
    a = sorted(a)
    a = [str(x) for x in a]
    return "".join(a)


for i in range(100, 1000):
    if f(i) == "71113":
        print(i)