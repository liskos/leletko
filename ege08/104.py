import itertools
b = 0
for i, a in enumerate(itertools.permutations("надпись", r=7), 1):
    s = "".join(a)
    if s[0] != "ь" and "ьиа" not in s:
        b = b + 1
print(b)