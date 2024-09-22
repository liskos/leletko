import itertools
b = set()
for a in itertools.permutations("одеколон", r=8):
    s = "".join(a)
    if "оо" not in s:
        b.add(s)
print(len(b))
