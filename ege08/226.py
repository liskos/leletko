import itertools
b = set()
for a in itertools.permutations("кусать", r=5):
    s = "".join(a)
    if s[0] != "ь" and "сук" not in s:
        b.add(s)
print(len(b))
