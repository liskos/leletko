import itertools
b = 0
for a in itertools.permutations("апорт", r=5):
    s = "".join(a)
    if "ао" not in s and "оа" not in s:
        b = b + 1

print(b)