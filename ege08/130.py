import itertools
b = 0
for a in itertools.permutations("есаул", r=5):
    s = "".join(a)
    s = s.replace("е", "1")
    s = s.replace("а", "1")
    s = s.replace("у", "1")
    if "11" not in s:
        b = b + 1

print(b)