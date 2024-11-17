def f(n):
    b = ""
    while n >0:
        b = b + str(n%4)
        n = n // 4
    return b.count("0")


a = int("723", 8) * int("b13a", 16) - int("10011101010", 2)
print(f(a))