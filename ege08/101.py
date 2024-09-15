import itertools
b = 0
for i, a in enumerate(itertools.permutations("шанель", r=6), 1):
    s = "".join(a)
    if s[0] != "ь" and "еаь" not in s:
        b = b + 1
print(b)