def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = "1" + b
    else:
        b += "0"
    if b.count('1') % 2 == 0:
        b += '1'
    else:
        b += '0'
    return int(b, 2)


for i in range(1, 1000):
    if f(i) > 228:
        print(i)
print(f(9))