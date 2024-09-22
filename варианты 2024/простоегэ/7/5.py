def s(n):
    s = ""
    while n > 0:
        s = s +  str(n % 3)
        n = n // 3
    return s[::-1]

def f(n):
    b = s(n)
    if n % 3 == 0:
        b = b + b[-2] + b[-1]
    else:
        b = b + s(n % 3 * 5)
    return int(b, 3)


a = set()
for i in range(1, 1000):
    if f(i) > 133:
        a.add(f(i))
print(f(11))
print(f(12))
print(min(a))