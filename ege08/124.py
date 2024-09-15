import itertools
b = 0
for a in itertools.permutations("чиуауа", r=6):
    b = b + 1
print(b)