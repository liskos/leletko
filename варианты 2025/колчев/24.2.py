import sys
sys.stdin=open("24.txt")
s = input()
d = s
d = d.replace("*", " ")
while "++" in d:
    d = d.replace("++", "+ +")

d = d.replace("*+", "").replace("+*", "").replace("+ "," ").replace(" +", " ")
d = d.split()
m = 0
for i in d:
    if "+" in i:
        m = max(m, eval(i))
print(m)