def f(n):
    b = ""
    a = "0123456789abcdefghijklmnopq"
    while n > 0:
        b = b + a[n%27]
        n = n // 27
    return b[::-1]



a = 5 * 729**2024 + 3 * 243**1413 - 7 * 81 **169 - 2 * 9 ** 107 + 3017
c = f(a)
c = c.replace("0", "")
c = c.replace("q", "")
print(c)