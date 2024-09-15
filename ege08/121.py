import itertools
b = set()
for a in itertools.permutations("тартар", r=6):
    b.add(a)
print(len(b))