import itertools
b = set()
for a in itertools.permutations("амфибрахий", r=10):
    s = "".join(a)
    if s[4] == "б" and s[5] == "р":
        b.add(s)
        print(s)
print(len(b))