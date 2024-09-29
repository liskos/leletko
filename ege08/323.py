def f(n):
    c = ""
    i = 0
    b = "хлбнймкш"
    while i < len(n):
        if n[i] in b:
            c = c + "1"
        else:
            c = c + n[i]
        i += 1
    return c


import itertools
b = set()
for a in itertools.product("70246", repeat=10):
    s = "".join(a)
    d = "быкиш"
    if s.count("7") == 5 and "77" not in s and s[0] != "0":
        b.add(s)
        print(s)
print(len(b))
