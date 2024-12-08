def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b = "10" + b[2:] + "0"
    else:
        b = "11" + b[2:] + "1"
    return int(b, 2)

print(f(6))
print(f(4))
for i in range(0, 100):
    if f(i) > 171:
        print(i)
        break