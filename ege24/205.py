s = open("24data/24-1.txt").read()
s = s.split("A")
r= []
for i in range(len(s)-5):
    r.append(len(s[i])+len(s[i+1])+len(s[i+2]) + len(s[i+3]) + len(s[i+4]) + len(s[i+5]) +5)

print(max(r))
