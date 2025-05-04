import itertools

for i,a in enumerate(itertools.product("абдеоп", repeat=6),1):
    s = "".join(a)
    if s[0] == "о" and s.count("а") <= 1 and s.count("б") <= 1 and s.count("д") <= 1 and s.count("е") <= 1 and s.count("о") <= 1 and s.count("п") <= 1:
        print(i)
        print(s)