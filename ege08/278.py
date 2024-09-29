import itertools
b = set()
for a in itertools.permutations("видео", r=6):
    s = "".join(a)
    d = s[:4]
    if s.count("и") >= 1 and s.count("е") >= 1:
        b.add(a)
        print(a)
print(len(b))