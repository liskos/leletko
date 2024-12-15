def f(n):
    b = ""
    while n > 0:
        b = b + str(n% 5)
        n = n // 5
    return b.count("0")


for x in range(1223):
    v = 4 ** x - 3 ** 331 + 9 ** 17
    if f(v) == 77:
        print(x)
        break