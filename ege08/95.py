import itertools
b = 0
for i, a in enumerate(itertools.permutations("кабинет", r=7), 1):
    s = "".join(a)
    if s[0] != "б" and "еа" not in s:
        b = b + 1
print(b)