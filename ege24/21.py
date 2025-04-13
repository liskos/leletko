s = open("24data/k7a-1.txt").read()
s = s.replace("D", " ").replace("E", " ").replace("F", " ")
s =s.split()
r = []
for i in s:
    r.append(len(i))

print(max(r))