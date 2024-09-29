import itertools
b = set()
for a in itertools.permutations("амфибрахий", r=10):
    s = "".join(a)
    if s[:2] == "ам" and s[-2:] == "ий":
        b.add(s)
        print(a)
print(len(b))