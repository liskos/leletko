import itertools
b = set()
for a in itertools.permutations("бархатка", r=8):
    s = "".join(a)
    s = s.replace("р", "б")
    s = s.replace("х", "б").replace("т", "б").replace("к", "б")
    if "аа" not in s and "бб" not in s:
        b.add(a)
        print(a)
print(len(b))
