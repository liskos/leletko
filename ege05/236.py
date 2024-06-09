def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b += "1"
    else:
        b += "0"
    if int(b, 2) % 2 == 0:
        b += "1"
    else:
        b += '0'
    return int(b, 2)


for i in range(1, 1000):
    if f(i) < 171:
        print(i)
print(f(9))