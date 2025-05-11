s = open("24data/24-157.txt").read()
s = s.replace("PR", "P R").replace("RP", "R P")
s = s.split()
r = []
for i in s:
    r.append(len(i))

print(max(r))