import itertools
b = set()
for a in itertools.permutations("мимикрия", r=8):
    s = "".join(a)
    b.add(s)
print(len(b))