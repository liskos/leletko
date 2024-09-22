import itertools
b = 0
for a in itertools.permutations("запись", r=6):
    s = "".join(a)
    if s[0] != "ь" and "аь" not in s and "иь" not in s:
        b += 1
print(b)
