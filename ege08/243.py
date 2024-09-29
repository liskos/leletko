import itertools
b = set()
for a in itertools.permutations("волкадав", r=8):
    s = "".join(a)
    s = s.replace("о", "а")
    s = s.replace("л", "в").replace("к", "в").replace("д", "в")
    if "аа" in s or "вв" in s:
        b.add(a)
        print(a)
print(len(b))