import itertools
r = []
for i, a in enumerate(itertools.product("аинптця", repeat=6), 1):
    if i % 2 == 0 and a[0] != "н" and a.count("я") == 2:
        r.append(a)
print(len(r))