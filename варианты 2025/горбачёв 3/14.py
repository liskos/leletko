def pere(n):
    b = ""
    while n > 0:
        b = b + str(n % 8)
        n = n // 8
    return b[::-1].count("1")


for x in range(1,3052+1):
    v = 4**151 + 7**283 + 6 ** 82 - 5 * x
    if pere(v) == 26:
        print(x)
        break