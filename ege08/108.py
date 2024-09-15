import itertools
b = 0
for a in itertools.permutations("комета", r=6):
    s = "".join(a)
    s = s.replace("т", "2")
    s = s.replace("м", "2")
    s = s.replace("к", "2")
    s = s.replace("о", "1")
    s = s.replace("е", "1")
    s = s.replace("а", "1")
    print(s)
    if "22" not in s and "11" not in s:
        b = b + 1
print(b)