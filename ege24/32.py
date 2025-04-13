s = open("24data/k7b-6.txt").read()
t = "DAF"
while t in s:
    t += "DAF"
while t not in s:
    t = t[:-1]
print(t in s, len(t))