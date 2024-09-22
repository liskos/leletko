import itertools
b = 0
for a in itertools.permutations("режимдно", r=6):
    s = "".join(a)
    d = "ржмдн"
    f = "еио"
    if (s[1] in f) and (s[0] in d) and (s[-1] in f):
        b += 1
        print(s)
print(b)