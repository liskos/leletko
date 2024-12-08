import itertools

k = 0
for a in itertools.product("авийкпс", repeat=6):
    s = "".join(a)
    if "аа" in s or "ии" in s or "аи" in s or "иа" in s:
        k += 1
    if s == "какааа":
        print(k)