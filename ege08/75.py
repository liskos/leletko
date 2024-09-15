import itertools

b = set()
for a in itertools.permutations("кораблик", r=6):
    s = "".join(a)
    ss = s.replace("р", "к").replace("б","к").replace("л", "к")
    ss = ss.replace("а", "о").replace("и", "о")
    if (ss[0] == "к") and ("кк" not in ss ) and ("оо" not in ss) and len(set(a)) == 6:
        b.add(s)
print(len(b))
