import itertools
b = set()
for a in itertools.permutations("абак", r=4):
    s = "".join(a)
    if "аа" not in s and "бб" not in s and "кк" not in s:
        b.add(s)
print(b)