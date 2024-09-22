import itertools
b = 0
for a in itertools.permutations("1п1льс1н", r=7):
    s = "".join(a)
    if ("1ь1" not in s) and ("1ь" not in s) and ("ь1" not in s) and s[-1] != "ь" and s[0] != "ь":
        b += 1
        print(s)
print(b)