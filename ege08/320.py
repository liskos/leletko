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
for a in itertools.permutations("хлебныймякиш", r=7):
    s = "".join(a)
    d = "быкиш"
    if s[0] == "х" and s[3] in d and "11" not in f(s):
        b.add(s)
        print(s)
print(len(b))
