import itertools
k = 0
for i in itertools.product("кзбс", repeat=5):
    s = "".join(i)
    if s.count("з") <=2 and "бк" not in s and "кб" not in s:
        k += 1


print(k)