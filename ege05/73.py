def f(n):
    a = [ int (x) for x  in str(n)]
    a[0] += 8
    a[1] += 5
    a[2] += 7
    a = sorted(a, reverse=True)
    a = [str(x) for x in a]
    return "".join(a)

for i in range(100, 1000):
    if f(i) == "16148":
        print(i)
        break

