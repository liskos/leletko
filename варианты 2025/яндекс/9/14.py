import string
def f(n):
    i = "0123456789abcdefghijklmno"
    b = ""
    while n >0:
        b = b + i[n%25]
        n = n // 25
    return b[::-1].count("0")

for x in range(900000,1000000+1):
    a = 25**340 + 25**79 - 5 ** 60 + x
    if f(a) == 287:
        print(x)