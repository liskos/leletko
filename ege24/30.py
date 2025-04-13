s = open("24data/k7b-4.txt").read()
t = "EBCF"
while t in s:
    t += "EBCF"
while t not in s:
    t = t[:-1]
print(t in s, len(t))