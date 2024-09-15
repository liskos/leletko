import itertools
b = set()
for a in itertools.product("abcd", repeat=3):
    s = "".join(a)
    if "ad" in s or "da" in s and "bc" not in s:
        b.add("".join(a))

print(len(b))