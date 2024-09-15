import itertools
b = 0
for i, a in enumerate(itertools.permutations("нигрол", r=6), 1):
    s = "".join(a)
    if s[0] != "о" and "оиг" not in s:
        b = b + 1
print(b)