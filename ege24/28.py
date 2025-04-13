s = open("24data/k7b-2.txt").read()
t = "DBAC"
while t in s:
    t += "DBAC"
while t not in s:
    t = t[:-1]
print(t in s, len(t))