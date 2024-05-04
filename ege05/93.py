def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    if b.count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    return int(b, 2)

a = []
for i in range(1, 100000):
    if f(i)>96:
        a.append(f(i))
print(min(a))