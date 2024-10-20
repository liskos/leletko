def pe(n):
    b = ""
    while n > 0:
        b = b + str(n % 5)
        n = n // 5
    return b[::-1]

a = int(pe(25 ** 61))
b = int(pe(5 ** 178))
for x in range(1, 2043):
    c = int(pe(x))
    d = a + b - c
    if str(d).count("0") == 60:
        print(x)
