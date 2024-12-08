def f(n):
    b = ""
    while n > 0:
        b = b + str(n%7)
        n = n // 7
    return b.count("6")


for x in range(0,1000):
    a = 7**666 + 7**333 + 49 ** x - 343
    if f(a) == 49:
        print(x)
        break