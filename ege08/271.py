import itertools
b = set()
for a in itertools.permutations("лооопрстт", r=8):
    s = "".join(a)
    if s[0] == "о" or s[-1] == "о":
        b.add(a)
print(len(b))
