import itertools
b = set()
for a in itertools.permutations("аврора", r=6):
    s = "".join(a)
    if "аа" not in s and "вв" not in s and "рр" not in s and "оо" not in s:
        b.add(s)
print(len(b))