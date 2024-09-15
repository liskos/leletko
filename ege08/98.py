import itertools
b = 0
for i, a in enumerate(itertools.permutations("гелий", r=5), 1):
    s = "".join(a)
    if s[0] != "й" and "ией" not in s:
        b = b + 1
print(b)