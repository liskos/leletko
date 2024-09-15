import itertools
b = 0
for a in itertools.permutations("аврора", r=6):
    s = "".join(a)
    if "аа" not in s and "вв" not in s and "рр" not in s and "оо" not in s:
        b = b + 1
print(b)