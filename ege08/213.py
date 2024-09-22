import itertools
b = set()
for a in itertools.permutations("тьюринг", r=6):
    s = "".join(a)
    if s[0] != "ь" and "иь" not in s and "юь" not in s:
        b.add(s)
print(len(b))