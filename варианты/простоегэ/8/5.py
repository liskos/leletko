def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b = "101" + b[3:] + "0"
    else:
        b = "10" + b[2:] + "11"
    return int(b, 2)

print(f(6))
print(f(4))
for i in  range(1, 1000):
    if f(i) > 68:
        print(i)