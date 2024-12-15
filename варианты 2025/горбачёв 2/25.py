def f(n):
    for d in reversed(range(113, n, 100)):
        if n % d == 0:
            return True, d
    return False, 0


k = 0
for i in range(300001, 10**10):
    ot, d = f(i)
    if ot:
        k += 1
        print(i, d)
        if k == 4:
            break