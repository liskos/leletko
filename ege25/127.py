def f(n):
    r = []
    if round(i**0.5) == i**0.5:
        k = 2
        while len(r) <2 and k < (n**0.5)-1:
            if n % k == 0:
                r.append(k)
            k += 1
    return r


for i in range(1523467,4157812):
    if len(f(i)) == 1:
        print(i, i // f(i)[0])