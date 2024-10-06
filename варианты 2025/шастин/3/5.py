def s(n):
    n = int(n)
    b = 0
    while n > 0:
        b = b + n % 10
        n = n // 10
    return b
def t(n):
    b = ""
    while n > 0:
        b = b + str(n % 3)
        n = n // 3
    return b[::-1]


def f(n):
    b = t(n)
    if s(b) % 2 == 0:
        b = "1" + b + "2"
    else:
        b = "2" + b + "1"
    return int(b, 3)


b = set()
for i in range(1, 10000):
    if f(i) > 100:
        b.add(f(i))
print(min(b))