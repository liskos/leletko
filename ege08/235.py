import itertools
b = set()
for a in itertools.permutations("аббатиса", r=8):
    s = "".join(a)
    s = s.replace("и", "а")
    s = s.replace("т", "б").replace("с", "б")
    if "аа" not in s and "бб" not in s:
        b.add(a)
        print(a)
print(len(b))
