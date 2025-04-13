import string
def f(n):
    k = 0
    c = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = "LMNOPQRSTUVWXYZ"
    while n > 0:
        if c[n%36] in b:
            k += 1
        n = n // 36
    return k

a = 9*57**2024+ 14 * 13 ** 3059 - 87 * 67 ** 1111 + 2027
print(f(a))
print("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[35])