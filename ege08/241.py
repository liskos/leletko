import itertools
b = set()
for a in itertools.permutations("аммиакат", r=7):
    s = "".join(a)
    s = s.replace("и", "а")
    s = s.replace("к", "м").replace("т", "м")
    if "аа" not in s and "мм" not in s:
        b.add(a)
        print(a)
print(len(b))