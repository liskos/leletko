import itertools
b = set()
for a in itertools.permutations("амфибрахий", r=10):
    s = "".join(a)
    if "аамии" in s or "иимаа" in s:
        b.add(s)
        print(s)
print(len(b))