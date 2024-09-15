import itertools
b = 0
for a in itertools.permutations("ассасин", r=7):
    b = b + 1
print(b)