def F(n):
    global  c
    c.append(n)
    if n > 0:
        d = (n%10 + F(n//10))
        c.append(n)
        return d
    else:
        return 0


for i in range(1, 10000):
    c = []
    F(i)
    if c[1] > 51:
        print(i, F(i))
        break
