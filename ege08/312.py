import itertools
b = set()
for a in itertools.permutations("амфибрахий", r=10):
    s = "".join(a)
    d = "мфбрх"
    if s[1] in d and s[3] in d and s[5] in d and s[7] in d and s[9] in d:
        b.add(s)
        print(s)
print(len(b))