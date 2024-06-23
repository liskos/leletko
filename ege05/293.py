def f(n):
    n = str(n) + "120"
    p1, p2 = 1, 1
    for i in range(len(n)):
        if int(n[i]) % 2 == 0 and int(n[i]) != 0:
            p1 = p1 * int(n[i])
        if int(n[i]) % 2 == 1 and int(n[i]) != 0:
            p2 = p2 * int(n[i])
    return abs(p1-p2)


for i in range(1, 1000):
    if f(i) == 29:
        print(i)
