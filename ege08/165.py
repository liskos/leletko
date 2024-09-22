import itertools
b = 0
for a in itertools.permutations(range(16), r=4):
    if a[0] != 0 and a[0] % 2 != a[1] % 2 != a[2] % 2 != a[3] % 2:
            b += 1
print(b)
