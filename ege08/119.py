import itertools
b = 0
for a in itertools.permutations("магистр", r=5):
    s = "".join(a)
    if s.count("а") + s.count("и") <= 1:
        b = b + 1
print(b)