s = open("24data/k7a-4.txt").read()
s = s.replace("D", " ")
s = s.split()
r = []
for i in s:
    r.append(len(i))

print(max(r))