s = open("24data/k7a-6.txt").read()
s = s.replace("A", " ").replace("E", " ")
s = s.split()
r = []
for i in s:
    r.append(len(i))

print(max(r))