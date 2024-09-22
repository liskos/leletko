import itertools
b = set()
for a in itertools.permutations("акарида", r=7):
    s = "".join(a)
    s = s.replace("и", "а")
    s = s.replace("р", "к").replace("д", "к")
    if "аа" not in s and "кк" not in s:
        b.add(a)
        print(a)
print(len(b))