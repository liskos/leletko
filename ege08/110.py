import itertools
b = 0
for a in itertools.permutations("рулька", r=6):
    s = "".join(a)
    if s[0] != "ь" and "уь" not in s and "аь" not in s:
        b = b + 1
print(b)