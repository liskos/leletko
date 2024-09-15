import itertools
b = set()
for a in itertools.product("abcd", repeat=3):
    s = "".join(a)
    if ("cb" not in s) and ("bc" not in s):
        if a[0] == "a" and a[1] == "d":
            b.add(s)
        elif a[1] == "a" and ( a[0] == "d" or a[2] == "d") and "aa" not in s:
            b.add(s)
        elif a[2] == "a" and a[1] == "d":
            b.add(s)
        elif "a" not in s:
            b.add(s)
print(b)
print(len(b))