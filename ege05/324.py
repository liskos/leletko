def f(n):
    b = bin(n)[2:]
    if int(b, 2) % 2 != 0 and b.count("1") % 2 == 1:
        b =  "1" + b
    else:
        b = b + str(b.count("1") % 2)
    if int(b, 2) % 2 != 0 and b.count("1") % 2 == 1:
        b =  "1" + b
    else:
        b = b + str(b.count("1") % 2)
    return int(b, 2)

print(f(12))
print(f(4))
for i in range(1, 1000):
    if f(i) < 100:
        print(i)