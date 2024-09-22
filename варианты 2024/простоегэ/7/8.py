import  itertools

a = set()
for i in itertools.permutations("0123456789", r=6):
    s = "".join(i)
    s1 = s.replace("0", "2").replace("4", "2").replace("6", "2").replace("8", "2")
    s1 = s1.replace("3", "1").replace("5", "1").replace("7", "1").replace("9", "1")
    if i[0] != "0" and int(s) % 5 == 0 and "22" not in s1 and "11" not in s1:
        a.add(s)
print(len(a))