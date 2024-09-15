import itertools

for i, a in enumerate(itertools.product("дкмо", repeat=5), 1):
    if "".join(a) == "домок" or "".join(a) == "комод":
        print(i)
print(493-238+1)