import itertools
b = set()
for a in itertools.permutations("лооопрстт", r=8):
    s = "".join(a)
    if s[0] != s[-1]:
        b.add(a)
print(len(b))
