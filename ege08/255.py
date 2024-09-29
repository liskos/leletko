def p(n):
    n = int(n)
    a = "01234567"
    b = ""
    while n > 0:
        b = b + str(a[n % 8])
        n = n // 8
    return b[::-1]


import itertools
b = set()
for a in itertools.product("0123456789", repeat=6):
    c = int("".join(a))
    if c % 2 == 0:
        s = p(c)
        if len(s) == 5 and s[0] == "7" and s.count("65") + s.count("56") == 1:
            b.add(a)
            print(s)
print(len(b))