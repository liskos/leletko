s = open("24data/24-153.txt").read()
s = s.replace("D"," ")
s =s.split()
r = []
for i in s:
    r.append(len(i))

print(min(r)+2)