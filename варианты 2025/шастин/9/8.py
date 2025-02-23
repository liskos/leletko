import itertools

for i, a in enumerate(itertools.product("геинрся", repeat=6), 1):
    s = "".join(a)
    if "гиря" in s:
        print(i)