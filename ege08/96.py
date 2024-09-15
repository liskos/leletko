import itertools
b = 0
for i, a in enumerate(itertools.permutations("комбайн", r=7), 1):
    s = "".join(a)
    if s[0] != "й" and "ай" not in s:
        b = b + 1
print(b)