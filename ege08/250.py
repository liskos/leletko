import itertools
for i, a in enumerate(itertools.product("еклост", repeat=5), 1):
    s = "".join(a)
    if s[0] == "с" and "оо" in s:
        print(a)
        print(i)
        break