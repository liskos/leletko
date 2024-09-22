import itertools
b = set()
for a in itertools.product("солнце", repeat=6):
    s = "".join(a)
    if s.count("о") <= 2 and s.count("ц") == 1:
        b.add(s)
print(len(b))