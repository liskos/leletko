import itertools
b = set()
for a in itertools.permutations("авторота", r=8):
    s = "".join(a)
    s = s.replace("о", "а")
    s = s.replace("т", "в").replace("р", "в")
    if "аа" not in s and "вв" not in s:
        b.add(a)
        print(a)
        print(s)
print(len(b))
