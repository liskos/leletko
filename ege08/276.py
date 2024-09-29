import itertools
b = set()
for a in itertools.permutations("спортлото", r=8):
    s = "".join(a)
    if s.count("тт") > 0:
        b.add(a)
print(len(b))