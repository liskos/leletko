import itertools
b = set()
for a in itertools.permutations("пскаль", r=4):
    s = "".join(a)
    if s[0] != "ь" and "ьь" not in s:
        b.add(s)
print(len(b))