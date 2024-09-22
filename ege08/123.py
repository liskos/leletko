import itertools
b = set()
for a in itertools.permutations("ассасин", r=7):
    b.add(a)
print(len(b))