s = open("24data/k7b-3.txt").read()
t = "BAFE"
while t in s:
    t += "BAFE"
while t not in s:
    t = t[:-1]
print(t in s, len(t))