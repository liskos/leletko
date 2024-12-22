def p(n):
    b = ""
    while n > 0:
        b = b + str(n % 4)
        n = n // 4
    return b[::-1]


def f(n):
    b = p(n)
    if n % 4 == 0:
        b = "2" + b + "03"
    else:
        b = b + p(n%4 * 5)
    return int(b, 4)

print(f(11))
print(f(4))
for i in range(10000):
    if f(i) <= 567:
        print(i)