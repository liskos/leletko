s = open("24data/k7b-1.txt").read()
t = "EAB"
while t in s:
    t += "EAB"
while t not in s:
    t = t[:-1]
print(t in s, len(t))