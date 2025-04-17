s = open("24data/k7a-2.txt").read()
s = s.replace("B", " ").replace("E", " ").replace("F", " ")
s =s.split()
r = []
for i in s:
    r.append(len(i))

print(max(r))