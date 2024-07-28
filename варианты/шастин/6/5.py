def p(n):
    b = ""
    while n > 0:
        b = b + str(n % 4)
        n = n // 4
    return b[::-1]

def f(n):
    b = p(n)
    if n % 3 == 0:
        b = b[-1] + b[1:-1] + b[0]
    else:
        b = b + str(n % 3)
    return int(b, 4)

print(f(11))
print(f(13))
a = set()
for i in range(1, 100):
    if f(i) <= 340 and i % 2 != 0:
        a.add(f(i))
print(max(a))
