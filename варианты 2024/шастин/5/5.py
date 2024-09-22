def p(n):
    r = ""
    while n > 0:
        r = r + str(n % 3)
        n = n // 3
    return  r[::-1]

def f(n):
    b = p(n)
    if n % 7 == 0:
        b = b + b[-2] + b[-1]
    else:
         b = b + str(p(n % 7 * 3))
    return int(b, 3)

print(f(11))
print(f(14))
a = set()
for i in range(1, 1000):
    if f(i) > 369:
        a.add(f(i))
print(min(a))