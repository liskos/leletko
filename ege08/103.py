import itertools
b = 0
for i, a in enumerate(itertools.permutations("купчиха", r=7), 1):
    s = "".join(a)
    if s[0] != "ч" and "иау" not in s:
        b = b + 1
print(b)