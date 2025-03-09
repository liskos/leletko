import string
def f(n):
    c = "0123456789abcdefghijklm"
    b = ""
    while n >0:
        b = b + c[n%23]
        n = n // 23
    return b[::-1]
a = 9 * 123**2053 + 5 * 23 ** 3146 + 91 * 47 ** 5533 + 4099
a = f(a)
def g(n):
    k = 0
    while len(n) > 0:
        if n[-1] in "ghijklm":
            k += 1
        n = n[:-1]
    return k

print(g(a))