import itertools
b = set()
for a in itertools.permutations("хочусотку ", r=9):
    s = "".join(a)
    if s[0] != " " and s[-1] != " " and s[0] != "у" and s.count(" ") == 1:
        b.add(s)
        print(s)
print(len(b))