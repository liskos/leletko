def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b = "1" + b + "00"
    else:
        b = "11" + b
    return int(b, 2)


a = set()
for i in range(1, 1000):
    if f(i) >= 412:
        a.add(i)
print(f(13))
print(min(a))