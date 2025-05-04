s = open("24data/24-153.txt").read()
s = s.replace("A"," ").replace("B", " ").replace("C", "").replace("E", " ").replace("F", "")
s =s.split()
r = []
for i in s:
    r.append(len(i))

print(min(r))