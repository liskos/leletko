def f(n):
    r = []
    if n % 2 != 0:
        k = 3
        while len(r) <71 and k < (n**0.5)+1:
            if n % k == 0:
                r.append(k)
            k += 2
    return r


for i in range(321654,654321):
    if len(f(i)) >= 36:
        print(i, i // f(i)[-1])