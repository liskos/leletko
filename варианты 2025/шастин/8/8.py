import itertools

r = set()
for i in itertools.permutations("парижанка", r=9):
    s = "".join(i)
    if (s.count("аа") + s.count("аи") + s.count("иа")) == 1 and "ааа" not in s:
        r.add(s)
print(len(r))
