s = open("24data/k7b-5.txt").read()
t = "CA"
while t in s:
    t += "CA"
while t not in s:
    t = t[:-1]
print(t in s, len(t))