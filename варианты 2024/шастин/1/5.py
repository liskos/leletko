def tr(n):
    t = "012"
    s = ""
    while n > 0:
        s = t[n % 3] + s
        n = n // 3
    return s

def f(n):
    t = tr(n)
    if n % 3 == 0:
        t = t + t[:2]
    else:
        t = t + tr(n % 3 * 5)
    return int(t, 3)


print(f(11), f(12))
a = []
for i in range(1, 1000):
    if f(i) > 64:
        a.append(f(i))
print(min(a))