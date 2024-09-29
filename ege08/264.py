import itertools
b = set()
for i, a in enumerate(itertools.permutations("лооопрстт", r=8), 1):
    s = "".join(a)
    if s[0] != "о" and s[-1] != "о" :
        b.add(a)
print(len(b))