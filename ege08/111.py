import itertools
b = 0
for a in itertools.permutations("айсберг", r=7):
    s = "".join(a)
    if s[0] != "й" and "ай" not in s and "ей" not in s:
        b = b + 1
print(b)