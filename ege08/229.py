import itertools
b = set()
for a in itertools.product("0123456", repeat=7):
    s = "".join(a)
    if s[0] != "0" and s[0] != "3" and s[0] != "5" and not (("22"  in s) and ("44"  in s)):
        b.add(s)
print(len(b))
