import itertools

b = set()
for a in itertools.permutations("таркнище", r=6):
    s = "".join(a)
    ss = s.replace("р", "т").replace("к","т").replace("н", "т").replace("щ", "т")
    ss = ss.replace("и", "а").replace("е", "а")
    if (ss[0] == "т") and ("тт" not in ss ) and ("аа" not in ss) and len(set(a)) == 6:
        b.add(s)
print(len(b))
