import itertools
b = set()
for a in itertools.permutations("марта", r=5):
    s = "".join(a)
    if "мм" not in s and "аа" not in s and "рр" not in s and "тт" not in s:
        b.add(s)
print(len(b))