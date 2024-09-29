import itertools
b = 0
for a in itertools.product("компьютер", repeat=6):
    s = "".join(a)
    if s.count("к") >= 1 and s.count("о") >= 1 and s.count("т") >= 1:
        b += 1
        print(s)
print(b)