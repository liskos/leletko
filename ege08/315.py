import itertools
b = 0
for a in itertools.permutations("хочуввуз  ", r=9):
    s = "".join(a)
    if s[0] != " " and s[-1] != " " and s[0] != "у" and s.count(" ") == 2 and "  " not in s:
        b += 1
        print(s)
print(b)