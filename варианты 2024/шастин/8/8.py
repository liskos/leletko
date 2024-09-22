import itertools
a = []
for i in itertools.product("алгоритм", repeat=6):
    if i.count("л") < 2 and i[0] != "р" and i[-1] in "аои":
        a.append(i)

print(len(a))