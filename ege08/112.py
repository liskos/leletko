import itertools
b = 0
for a in itertools.permutations("вентиль", r=7):
    s = "".join(a)
    if s[0] != "ь" and "еьи" not in s and "иье" not in s:
        b = b + 1
print(b)