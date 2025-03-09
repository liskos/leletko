def f(n):
    r = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            r.add(i)
            r.add(n//i)
    r = [i for i in r if str(i)[-2:] == "14" and i != 14]
    return min(r) if r else 0

k = 0
for i in range(800000, 10 ** 10):
    if f(i) != 0:
        print(i,f(i))
        k += 1
        if k == 5:
            break
