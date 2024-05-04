def ch(n):
    t = "0123"
    s = ""
    while n > 0:
        s = t[n % 4] + s
        n = n // 4
    return s


def f(n):
    c = ch(n)
    if len(c) % 2 == 0:
        c = c[:len(c)//2] + "0" + c[len(c)//2:]
    return int(c)


for i in range(1, 10000):
    if f(i) <= 180:
        print(i)