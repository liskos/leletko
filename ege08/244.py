import itertools
b = set()
for a in itertools.permutations("шарлатан", r=8):
    s = "".join(a)
    s = s.replace("р", "ш").replace("л", "ш").replace("т", "ш").replace("н", "ш")
    if "аа" in s or "шш" in s:
        b.add(a)
        print(a)
print(len(b))