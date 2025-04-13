s = open("24data/k7b-3.txt").read()
t = "BAFF"
while t in s:
    t += "BAFF"
while t not in s:
    t = t[:-1]
print(t in s, len(t))