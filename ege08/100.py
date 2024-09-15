import itertools
b = 0
for i, a in enumerate(itertools.permutations("панель", r=6), 1):
    s = "".join(a)
    if s[0] != "ь" and "еап" not in s:
        b = b + 1
print(b)