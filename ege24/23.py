s = open("24data/k7a-3.txt").read()
s = s.replace("D", " ").replace("C", " ")
s =s.split()
r = []
for i in s:
    r.append(len(i))

print(max(r))