def f(n):
    r = []
    k= 2
    while len(r) <3 and k < (n**0.5)-1:
        if n % k == 0:
            r.append(k)
        k += 1
    return r


for i in range(152346,957812):
    if len(f(i)) == 1 and i**0.5 == int(i**0.5):
        print(i, i // f(i)[0])
