def p(n):
    r = ""
    while n > 0:
        r = r + str(n % 4)
        n //= 4
    return r[::-1]

def f(n):
    b = str(n % 2) + p(n) + str(n % 3)
    return int(b, 4)


print(f(23))
for i in range(1, 1000):
    if f(i) < 100:
        print(f(i))