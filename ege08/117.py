import itertools
b = 0
for a in itertools.permutations("кабала", r=6):
    s = "".join(a)
    if "кк" not in s and "аа" not in s and "бб" not in s and "лл" not in s:
        b = b + 1
print(b)