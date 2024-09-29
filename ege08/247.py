import itertools
b = set()
for a in itertools.product("лог", repeat=20):
    s = "".join(a)
    if "гг" not in s and "оо" not in s and "лл" not in s and s[0] != "г" and s[-1] != "г":
        if "ого" not in s and "лгл" not in s:
            b.add(a)
            print(a)
print(len(b))