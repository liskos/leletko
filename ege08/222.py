import itertools
b = set()
for a in itertools.permutations("зер1111ало", r=6):
    s = "".join(a)
    if 0 < s.count("1") <= 4:
        b.add(s)
print(len(b))
