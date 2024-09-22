import itertools
b = set()
for a in itertools.permutations("клабхаус", r=8):
    s = "".join(a)
    if "аа" not in s:
        b.add(s)
print(len(b))