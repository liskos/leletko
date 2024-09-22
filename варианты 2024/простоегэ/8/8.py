import itertools


r = []
for a in itertools.permutations("0234567", r=5):
    s = "".join(a).replace("4", "2").replace("6", "2").replace("0", "2")
    s = s.replace("3", "1").replace("5", "1").replace("7", "1")
    if a[0] != "0" and "22" not in s and "11" not in s:
        r.append(a)
print(len(r))
