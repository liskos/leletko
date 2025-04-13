s = open("24data/k7-40.txt").read()
t = "C"
while t in s:
    t += "C"

print(len(t)-1)