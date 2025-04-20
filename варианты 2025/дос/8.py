import itertools

k = 0
for a in itertools.product("ДГИАШЭ", repeat=5):
    s = "".join(a)
    if s[0] not in "АИЭ" and s[-1] not in "ДГШ":
        k += 1

print(k)  