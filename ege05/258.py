def f(n):
    b = bin(n)[2:]
    c = b + str(b.count("1") % 2)
    if b.count("1") > b.count("0"):
        c += "0"
    else:
        c += "1"
    return int(c, 2)


a = set()
for i in range(1, 100):
    if 50 <= f(i) <= 80:
        a.add(f(i))
print(len(a))
print(a)