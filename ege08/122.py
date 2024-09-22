import itertools
b = set()
for a in itertools.permutations("молоко", r=6):
    b.add(a)
print(len(b))