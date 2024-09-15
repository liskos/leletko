import itertools
b = 0
for a in itertools.permutations("марта", r=5):
    s = "".join(a)
    if "мм" not in s and "аа" not in s and "рр" not in s and "тт" not in s:
        b = b + 1
print(b)