
import itertools
b = 0
for a in itertools.permutations("аджика", r=6):
    s = "".join(a)
    if "аа" not in s and "дд" not in s and "жж" not in s and "ии" not in s and "кк" not in s:
        b = b + 1
print(b)