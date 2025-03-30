def fp(n):
    n = int(n)
    p = 1
    while n > 0:
        p = p * (n % 10)
        n = n // 10
    return p



def f(n):
    s = str(n)
    s = s.replace("3", "4")
    s = s.replace("7", "8")
    return fp(s)

for i in range(1000,10000):
    if f(i) == 256:
        print(i)
        break
