def p(n):
    a = ""
    t = "0123456789abcdef"
    while n > 0:
        a = a + t[n % 16]
        n = n // 16
    return a[::-1]

def f(n):
    b = p(n // 2)
    if n % 4 == 0:
        b = "15" + b + "c"
    else:
        b = "f" + b + "a0"
    return int(b, 16)


for i in range(1, 1000):
    if f(i) < 65536:
        print(i)

print(f(4))