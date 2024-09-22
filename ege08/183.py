import itertools
b = 0
for a in itertools.permutations("0123456789abcdef", r=15):
    s = "".join(a)
    d = int(s, 15)


print(b)
