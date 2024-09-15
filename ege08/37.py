import itertools

for i, a in enumerate(itertools.product("акру", repeat=5), 1):
    if "".join(a) == "рукаа" or "".join(a) == "укара":
        print(i)