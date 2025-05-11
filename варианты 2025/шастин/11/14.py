import string
def f(n):
    t = "0123456789ABCDEFG"
    b = ""
    while n > 0:
        b = b + t[n%17]
        n = n // 17
    return b[::-1]


a = 3 * 17 ** 777 + 15 * 17 ** 250 - 6 * 17 ** 100 + 2
r = f(a)
k = len(set([x for x in r if int(x,17) % 2 == 0]))
print(k)
