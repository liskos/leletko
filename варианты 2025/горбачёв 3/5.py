def f(n):
    b = bin(n)[2:]
    if b.count("1") % 4 == 0:
        b = "10" + b[2:] + "01"
    else:
        b = "11" + b[1:] + "1"
    return int(b,2)


print(f(12))
print(f(6))
for i in range(1,1000):
    if f(i) >= 127:
        print(i)
        break
