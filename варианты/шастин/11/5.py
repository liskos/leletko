def s(n):
    n = int(n)
    b = 0
    while n > 0:
        b = b + n % 10
        n = n // 10
    return b
def pe(n):
    b = ""
    d ="012"
    while n > 0:
        b = b + d[n % 3]
        n = n // 3
    return b[::-1]

def f(n):
    n = pe(n)
    if s(n) % 3 == 0:
        n = n + "212"
    else:
        n = n + pe(s(n * 2))
    return int(n, 3)

print(f(11))
print(f(12))
b = set()
for i in range(1, 1000):
    if f(i) > 490:
        b.add(f(i))
print(min(b))
