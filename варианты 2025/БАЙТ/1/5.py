def su(n):
    s = 0
    while len(n) > 0:
        s = s + int(n[-1])
        n = n[:-1]
    return s


def g(n):
    b = ""
    while n > 0:
        b = b + str(n % 5)
        n =n // 5
    return b[::-1]

def f(n):
    b = g(n)
    if n % 5 == 0:
        b = b[0] + b + b[-1]
    else:
        s = su(b)
        b = b + g(s)
    return  int(b,5)

print(f(50))
print(f(55))
r = []
for i in range(50,101):
    if f(i) % 5 == 0:
        r.append(f(i))

print(max(r))