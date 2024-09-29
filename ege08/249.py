import itertools
for i, a in enumerate(itertools.product("апрсу", repeat=5), 1):
    s = "".join(a)
    if s[0] == "у" and s.count("а") == 2 and "аа" not in s:
        print(a)
        print(i)
        break
