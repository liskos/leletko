import itertools
b = 0
for a in itertools.product("ясновидец", repeat=5):
    s = "".join(a)
    d = "снвдц"
    f = "яоие"
    if s.count(s[0]) == 1 and s.count(s[-1]) == 1 and (s[0] in d) and (s[-1] in f):
        b += 1
        print(s)
print(b)