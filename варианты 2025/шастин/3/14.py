def t(n):
    b = ""
    while n > 0:
        b = b + str(n % 5)
        n = n // 5
    return b[::-1]

for i in range(0, 5556):
    a = 5 ** 150 + 5 ** 135 - i
    d = t(a)
    if d.count("4") == 134:
        print(i)