import itertools
b = 0
for a in itertools.permutations("абрикос", r=7):
    s = "".join(a)
    s = s.replace("б", "2")
    s = s.replace("р", "2")
    s = s.replace("к", "2")
    s = s.replace("с", "2")
    s = s.replace("и", "1")
    s = s.replace("о", "1")
    s = s.replace("а", "1")
    print(s)
    if "22" not in s and "11" not in s:
        b = b + 1
print(b)