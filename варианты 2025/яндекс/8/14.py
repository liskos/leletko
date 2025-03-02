def f(n):
    b = ""
    c = "0123456789abcdefghijklmno"
    while n > 0:
        b = b + c[n%25]
        n = n // 25
    return b[::-1]

a = 625**90 + 125**120 - 5 * 25
v = f(a).count("o") * 24 + 20
print(v)
print(f(a))