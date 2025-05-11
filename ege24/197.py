s = open("24data/24-197.txt").read()
s = s.replace("XX", "X ").replace("YY", "Y ").replace("ZZ", " Z")
s = s.split()
r = []
for i in s:
    r.append(i.count("ZX") + i.count("ZY"))

print(max(r))