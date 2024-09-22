import itertools
b = set()
for a in itertools.permutations("соткаплз", r=5):
    s = "".join(a)
    if "зло" not in s and s[-1] != "о" and s[-1] != "а":
        b.add(s)
print(len(b))