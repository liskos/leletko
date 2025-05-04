s = open("24data/24-157.txt").read()
t = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
r = []
for x in t:
    k = 0
    for i in t:
        k += s.count(f"{x}{i}{i}")
    r.append([k,str(x)+str(k)])


print(max(r))