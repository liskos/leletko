s = open("24data/24-5.txt").read()
t = "("
while t in s:
    t += "("

print(len(t)-1)