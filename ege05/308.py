def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        c = b[-4:].replace("1", "2")
        c = c.replace("0", "1")
        c = c.replace("2", "0")
        b =  b[:-4] + c
    else:
        c = b[-5:-1]
        c = c.replace("1", "2")
        c = c.replace("0", "1")
        c = c.replace("2", "0")
        b = b[:-5] + c + b[-1]
    return int(b, 2)

a = dict()
for i in range(64, 100):
    if f(i) in a:
        a[f(i)] = min(i, a[f(i)])
    else:
        a[f(i)] = i
print(min(a), a[min(a)])




