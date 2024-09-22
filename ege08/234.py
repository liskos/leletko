import itertools
b = set()
for a in itertools.permutations("академик", r=8):
    s = "".join(a)
    s = s.replace("е", "а").replace("и", "а")
    s = s.replace("д", "к").replace("м", "к")
    if "аа" not in s and "кк" not in s:
        b.add(a)
print(len(b))
