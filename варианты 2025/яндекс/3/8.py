import itertools

k = 0
d = 0
for i in itertools.permutations("артём", r=5):
    s = "".join(i)
    k += 1
    if s[0] in "аё" and s[-1] in "аё":
        d += 1

print(k - d)