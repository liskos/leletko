import itertools
b = 0
for i, a in enumerate(itertools.permutations("нода", r=4), 1):
    s = "".join(a)
    if "ао" not in s and "оа" not in s and "нд" not in s and "дн" not in s:
        b = b + 1
print(b)