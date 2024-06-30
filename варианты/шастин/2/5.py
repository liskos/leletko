def pr(n):
    b = ""
    while n > 0:
        b = b + str(n % 7)
        n = n // 7
    return b[::-1]


def f(n):
    b = pr(n)
    if b.count("2") % 2 == 0:
        b = b + "555"
    else:
        b = "1" + b
    return int(b, 7)

print(f(11))
print(f(14))
for i in range(1, 10000000):
    if f(i) < 3799:
        print(i)