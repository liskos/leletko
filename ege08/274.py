import itertools
b = set()
for a in itertools.permutations("лооопрстт", r=8):
    s = "".join(a)
    if s.count("оо") > 0:
        b.add(a)
print(len(b))
