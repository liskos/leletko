import itertools

k = 0
for i in itertools.product("abehc", repeat=5):
    s = "".join(i)
    if s[0] == "h" and s.count("b") == 2 and len(set(s)) == 4:
        k += 1

print(k)