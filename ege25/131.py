def f(n):
    r = []
    if round(i**0.5) == i**0.5:
        k = 2
        while len(r) <2 and k < (n**0.5)-1:
            if n % k == 0:
                r.append(k)
            k += 1
    return r


for i in range(106732567,152673836):
    if len(f(i)) == 1 and i**0.5 == int(i**0.5):
        print(i, i // f(i)[0])