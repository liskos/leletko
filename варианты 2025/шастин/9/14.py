def f(n):
    n = int(n)
    b = ""
    while n > 0:
        b = b + str(n % 7)
        n = n // 7
    return b[::-1]

r = []
o = []
for x in range(1,10000):
    a = 7 ** 270 + 7 ** 170 + 7 ** 70 - x
    r.append(f(a).count("0"))

for x in range(1,10000):
    a = 7 ** 270 + 7 ** 170 + 7 ** 70 - x
    if f(a).count("0") == max(r):
        o.append(x)

print(max(o))