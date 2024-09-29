import itertools
b = set()
for a in itertools.permutations("амфибрахий", r=10):
    s = "".join(a)
    if "аа" in s or "ии" in s:
        b.add(s)
        print(s)
print(len(b))