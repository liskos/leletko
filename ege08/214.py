import itertools
b = set()
for a in itertools.permutations("вайфу", r=4):
    s = "".join(a)
    if s[0] != "й" and "вф" not in s and "фв" not in s:
        b.add(s)
print(len(b))