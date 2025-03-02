def f(n):
    r = []
    for i in range(1, n):
        if n % i == 0 and str(i)[-2:] == "14" and n != i and i != 14:
            r.append(i)
    if len(r) > 0:
        return min(r)
    else:
        return 1

k = 0
for i in range(800000, 10 ** 10):
    if f(i) != 1:
        print(i,f(i))
        k += 1
        if k == 5:
            break
print(f(800026))