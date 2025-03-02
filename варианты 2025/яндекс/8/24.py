s = open("24(1).txt").read()
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    s = s.replace(i, " ")
a = []
for i in s.split():
    if i[0] != "0" and i[-1] in "02468":
        a.append(int(i))
print(max(a))