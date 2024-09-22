import itertools
b = 0
for a in itertools.permutations("дейкстра", r=6):
    s = "".join(a)
    if "йе" not in s and "йа" not in s and s[-1] != "й" and s.count("й") == 1:
        b += 1
        print(s)
print(b)