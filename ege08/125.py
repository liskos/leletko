import itertools
b = set()
for a in itertools.permutations("тратата", r=7):
    b.add(a)
print(len(b))