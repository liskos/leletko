import itertools
b = set()
for a in itertools.permutations("марина", r=6):
    s = "".join(a)
    if s[0] != "а" and s[0] != "и":
        b.add(s)
print(len(b))
