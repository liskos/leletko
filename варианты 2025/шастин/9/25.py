def f(n):
    r = []
    d = 2
    c = n
    while d * d <= n:
        if n % d == 0:
            r.append(d)
            n //= d
        else:
            d += 1
    if n > 1 and n != c:
        r.append(n)
    if len(r) > 0:
        return max(r) - min(r)


for i in range(3333338, 10**10):
    if f(i) > 1000 and f(i) % 3 == 0:
        print(i,f(i))