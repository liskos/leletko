def s(n):
    b = int(n)
    s = 0
    while b > 0:
        s = s + b % 10
        b = b // 10
    return s


def p(n):
    b = ""
    while n > 0:
        b = b + str(n%9)
        n = n // 9
    return b[::-1]

def f(n):
    b = p(n)
    if s(b) % 2 == 0:
        b = b + "52"
    else:
        b = "73" + b[2:] + "44"
    return int(b, 9)

print(f(11))
for i in range(1, 1000):
    if f(i) > 13950:
        print(i)
        break