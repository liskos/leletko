import itertools
b = 0
for a in itertools.permutations("пескарь", r=7):
    s = "".join(a)
    if s[0] != "ь" and "ье" not in s and "ьа" not in s and "ьр" not in s:
        b = b + 1
print(b)