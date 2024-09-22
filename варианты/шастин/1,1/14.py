def f(n):
    b = ""
    while n > 0:
        b = b + str(n % 4)
        n = n // 4
    return b

a = 4 ** 644 + 4 ** 322 + 16 ** 35 - 64 ** 3
c = f(a)
print(c.count("3"))

