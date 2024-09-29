import itertools
b = set()
for a in itertools.product("егэинф", repeat=6):
    s = "".join(a)
    if s[0] == "е" and s[-1] in "эи" and s.count("фи") >= 2 and "егэ" not in s:
        b.add(a)
        print(a)
print(len(b))
