import string
s = open("24data/24-307.txt").read()
s = s.replace("++", " ").replace("**", " ")
t = "ACDEFGHIJKLMNOPQRSTUVWXYZ"
for i in t:
     s = s.replace(f"{i}", " ")

s = s.replace(" +", " ").replace(" *", " ").replace(" 0", " ").replace("+0", " ").replace("*0", " ")
s = s.split()
r = []
for i in s:
    if i[-1] == "B":
        r.append([len(i),i])

print(max(r))