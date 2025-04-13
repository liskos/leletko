s = open("24data/k7a-5.txt").read()
s = s.replace("C", " ").replace("F", " ")
s = s.split()
r = []
for i in s:
    r.append(len(i))

print(max(r))