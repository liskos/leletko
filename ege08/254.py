def p(n):
    n = int(n)
    a = "0123456789abcdef"
    b = ""
    while n > 0:
        b = b + str(a[n % 16])
        n = n // 16
    return b[::-1]


import itertools
b = set()
for a in itertools.product("0123456789", repeat=8):
    c = int("".join(a))
    s = p(c)
    if len(s) == 5 and s[0] == "f" and s[-1] == "a" and s.count("3b") == 1:
        b.add(a)
        print(s)
print(len(b))