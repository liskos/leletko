import itertools
b = 0
for i, a in enumerate(itertools.permutations("крой", r=4), 1):
    s = "".join(a)
    if s[0] != "й" and "ой" not in s:
        b = b + 1
print(b)