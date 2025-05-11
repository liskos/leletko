import re
s = open("24data/24-215.txt").read()
s = s.replace("B", "A").replace("C", "A").replace("AA", "A")
s = s.replace("2", "1").replace("3", "1")
t = "A11"
while t in s:
    t += "A11"



print((len(t)-3)/3)
