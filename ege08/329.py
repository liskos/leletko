def f(n):
    c = ""
    i = 0
    b = "тмфй"
    while i < len(n):
        if n[i] in b:
            c = c + "1"
        else:
            c = c + n[i]
        i += 1
    return c

import itertools
b = set()
for a in itertools.product("тимофей", repeat=6):
    s = "".join(a)
    d = f(s)
    if d.count("1") == (len(s) - d.count("1")):
        b.add(s)
        print(s)
print(len(b))