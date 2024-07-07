def F(n):
    b = 0
    if n > 0:
        b = n % 10 * F(n // 10)
    else: return 1
    return b


for i in range(1, 1000):
    if F(i) > 320:
        print(i)