import itertools
b = 0
for i, a in enumerate(itertools.permutations("нобелий", r=7), 1):
    s = "".join(a)
    if s[0] != "й" and "ийо" not in s:
        b = b + 1
print(b)