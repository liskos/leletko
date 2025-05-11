s = open("24data/24-181.txt").read()
s = s.replace(".", " ")
s = s.split()
r = []
for i in s:
    if i.count("A") >= 3:
        r.append(len(i))
print(max(r))