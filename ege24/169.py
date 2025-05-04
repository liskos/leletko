s = open("24data/24-169.txt").read()
t = "XYZ"
while t in s:
    t += "XYZ"

print(len(t)-3)